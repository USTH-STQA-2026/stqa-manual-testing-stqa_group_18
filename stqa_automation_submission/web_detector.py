"""Automatically detect web technology and choose an interaction strategy.

Supported detections:
  - Flutter Web (CanvasKit / HTML renderer)
  - React / Next.js
  - Angular
  - Vue.js / Nuxt.js
  - Static HTML

Usage:
    from web_detector import detect_technology, WebTech
    tech = detect_technology(page)
    print(tech.name, tech.renderer)
"""
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class TechName(str, Enum):
    FLUTTER = "Flutter Web"
    REACT = "React"
    NEXTJS = "Next.js"
    ANGULAR = "Angular"
    VUE = "Vue.js"
    NUXTJS = "Nuxt.js"
    SVELTE = "Svelte"
    STATIC_HTML = "Static HTML"
    UNKNOWN = "Unknown"


class FlutterRenderer(str, Enum):
    CANVASKIT = "CanvasKit"
    HTML = "HTML"
    UNKNOWN = "Unknown"


@dataclass
class WebTech:
    name: TechName
    renderer: Optional[str] = None  # For Flutter (CanvasKit / HTML)
    version: Optional[str] = None
    evidence: list = field(default_factory=list)  # Detection evidence list

    @property
    def is_flutter(self) -> bool:
        return self.name == TechName.FLUTTER

    @property
    def is_flutter_canvaskit(self) -> bool:
        return self.name == TechName.FLUTTER and self.renderer == FlutterRenderer.CANVASKIT

    @property
    def needs_semantics(self) -> bool:
        """Flutter CanvasKit needs the semantics tree for interaction."""
        return self.is_flutter_canvaskit

    @property
    def uses_standard_dom(self) -> bool:
        """Return whether the page uses a standard HTML DOM."""
        return not self.is_flutter_canvaskit

    def summary(self) -> str:
        lines = [f"Technology: {self.name.value}"]
        if self.renderer:
            lines.append(f"Renderer: {self.renderer}")
        if self.version:
            lines.append(f"Version: {self.version}")
        lines.append(f"Standard DOM: {'Yes' if self.uses_standard_dom else 'No'}")
        lines.append(f"Needs Semantics: {'Yes' if self.needs_semantics else 'No'}")
        if self.evidence:
            lines.append(f"Evidence: {', '.join(self.evidence)}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Detection logic
# ---------------------------------------------------------------------------

def _detect_flutter(page) -> Optional[WebTech]:
    """Detect Flutter Web and determine its renderer."""
    evidence = []

    has_flutter_view = page.locator("flutter-view").count() > 0
    has_flt_glass = page.locator("flt-glass-pane").count() > 0
    has_flt_scene = page.locator("flt-scene").count() > 0
    has_bootstrap = page.evaluate("typeof _flutter !== 'undefined' || !!document.querySelector('script[src*=\"flutter\"]')")

    if has_flutter_view:
        evidence.append("<flutter-view>")
    if has_flt_glass:
        evidence.append("<flt-glass-pane>")
    if has_flt_scene:
        evidence.append("<flt-scene>")
    if has_bootstrap:
        evidence.append("flutter_bootstrap.js")

    if not evidence:
        return None

    # Determine renderer.
    has_canvas = page.locator("canvas").count() > 0
    renderer = FlutterRenderer.CANVASKIT if has_canvas else FlutterRenderer.HTML
    if has_canvas:
        evidence.append("CanvasKit (<canvas>)")
    else:
        evidence.append("HTML renderer")

    return WebTech(
        name=TechName.FLUTTER,
        renderer=renderer,
        evidence=evidence,
    )


def _detect_react(page) -> Optional[WebTech]:
    """Detect React / Next.js."""
    evidence = []
    is_react = page.evaluate("""() => {
        if (window.__REACT_DEVTOOLS_GLOBAL_HOOK__) return 'devtools';
        if (document.querySelector('[data-reactroot]')) return 'reactroot';
        if (document.querySelector('#__next')) return 'nextjs';
        const el = document.querySelector('body > div');
        if (el && el._reactRootContainer) return 'rootContainer';
        return null;
    }""")

    if not is_react:
        return None

    is_nextjs = page.evaluate("!!document.querySelector('#__next') || !!window.__NEXT_DATA__")
    if is_nextjs:
        evidence.append("__NEXT_DATA__ / #__next")
        version = page.evaluate("window.__NEXT_DATA__?.buildId || null")
        return WebTech(name=TechName.NEXTJS, version=version, evidence=evidence)

    evidence.append(f"React detected via: {is_react}")
    return WebTech(name=TechName.REACT, evidence=evidence)


def _detect_angular(page) -> Optional[WebTech]:
    """Detect Angular."""
    evidence = []
    is_angular = page.evaluate("""() => {
        if (window.ng) return 'ng';
        if (document.querySelector('[ng-version]')) return 'ng-version';
        if (document.querySelector('app-root')) return 'app-root';
        if (document.querySelector('[_nghost]') || document.querySelector('[_ngcontent]')) return 'ngcontent';
        return null;
    }""")

    if not is_angular:
        return None

    version = page.evaluate("document.querySelector('[ng-version]')?.getAttribute('ng-version') || null")
    evidence.append(f"Angular detected via: {is_angular}")
    return WebTech(name=TechName.ANGULAR, version=version, evidence=evidence)


def _detect_vue(page) -> Optional[WebTech]:
    """Detect Vue.js / Nuxt.js."""
    evidence = []
    is_vue = page.evaluate("""() => {
        if (window.__VUE__) return 'vue3';
        if (window.Vue) return 'vue2';
        if (document.querySelector('[data-v-]') || document.querySelector('[data-v-app]')) return 'data-v';
        if (document.querySelector('#__nuxt') || window.__NUXT__) return 'nuxt';
        return null;
    }""")

    if not is_vue:
        return None

    is_nuxt = page.evaluate("!!document.querySelector('#__nuxt') || !!window.__NUXT__")
    if is_nuxt:
        evidence.append("__NUXT__ / #__nuxt")
        return WebTech(name=TechName.NUXTJS, evidence=evidence)

    evidence.append(f"Vue detected via: {is_vue}")
    return WebTech(name=TechName.VUE, evidence=evidence)


def _detect_svelte(page) -> Optional[WebTech]:
    """Detect Svelte / SvelteKit."""
    is_svelte = page.evaluate("""() => {
        const els = document.querySelectorAll('[class]');
        for (const el of els) {
            for (const cls of el.classList) {
                if (cls.startsWith('svelte-')) return true;
            }
        }
        return !!document.querySelector('[data-sveltekit]') || !!window.__sveltekit;
    }""")
    if not is_svelte:
        return None
    return WebTech(name=TechName.SVELTE, evidence=["svelte- class prefix"])


def detect_technology(page) -> WebTech:
    """Detect the web technology used by the current page.

    Args:
        page: Playwright Page object that has already navigated to the URL.

    Returns:
        WebTech object containing the detected technology information.
    """
    # Priority order: detect Flutter first because it has the most unusual DOM.
    detectors = [
        _detect_flutter,
        _detect_angular,  # Detect Angular before React to avoid false positives from devtools hooks.
        _detect_vue,
        _detect_svelte,
        _detect_react,
    ]

    for detector in detectors:
        try:
            result = detector(page)
            if result:
                return result
        except Exception:
            continue

    # Fallback: check whether this is plain/static HTML.
    has_forms = page.locator("form").count() > 0
    has_inputs = page.locator("input, textarea, select").count() > 0
    if has_forms or has_inputs:
        return WebTech(name=TechName.STATIC_HTML, evidence=["Standard HTML form elements"])

    return WebTech(name=TechName.UNKNOWN)


# ---------------------------------------------------------------------------
# Test automation strategy comparison across technologies
# ---------------------------------------------------------------------------

COMPARISON = """
╔══════════════════════════════════════════════════════════════════════════════════╗
║              TEST AUTOMATION COMPARISON: Flutter Web vs Standard HTML          ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  ┌─────────────────┬──────────────────────────┬─────────────────────────────┐   ║
║  │    Criterion    │      Standard HTML /     │      Flutter Web            │   ║
║  │                 │   React / Angular / Vue  │    (CanvasKit renderer)     │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ Rendering       │ DOM-based                │ Canvas pixel rendering      │   ║
║  │                 │ Each element = DOM node  │ Entire UI = one <canvas>    │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ DOM Elements    │ Yes: <input>, <button>, │ No HTML elements           │   ║
║  │                 │    <div>, <a>, ...        │    by default              │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ CSS Selectors   │ Work normally            │ Not usable without         │   ║
║  │                 │    #id, .class, tag       │    exposed elements         │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ XPath           │ Works                    │ Not usable by default      │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ Input strategy  │ page.fill('input', val)  │ 1. Enable Semantics        │   ║
║  │                 │ page.click('button')     │ 2. Locate by aria-label    │   ║
║  │                 │                          │ 3. Fill qua flt-editing     │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ Click strategy  │ page.click('#btn')       │ Click flt-semantics with   │   ║
║  │ button          │ page.click('text=Login') │ role="button"              │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ Waiting         │ wait_for_selector        │ Needs explicit waits       │   ║
║  │                 │ wait_for_load_state      │ because Flutter is async    │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ Screenshot      │ Normal screenshots       │ Works with canvas          │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ Text assertion  │ page.content() has text  │ Text appears in semantics  │   ║
║  │                 │                          │ only after enabling it      │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ Inspect element │ DevTools Elements tab    │ Only <canvas> visible      │   ║
║  │ (DevTools)      │    shows full DOM tree    │    Enable semantics first   │   ║
║  ├─────────────────┼──────────────────────────┼─────────────────────────────┤   ║
║  │ Test speed      │ Fast                     │ Slower due to canvas       │   ║
║  │                 │                          │ rendering and semantics     │   ║
║  └─────────────────┴──────────────────────────┴─────────────────────────────┘   ║
║                                                                                ║
╚══════════════════════════════════════════════════════════════════════════════════╝
"""


def print_comparison():
    """Print the comparison table to the console."""
    print(COMPARISON)


# ---------------------------------------------------------------------------
# CLI: run directly to detect the technology of a URL
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    from playwright.sync_api import sync_playwright

    url = sys.argv[1] if len(sys.argv) > 1 else "https://stqa.rbc.vn"

    print(f"\nAnalyzing: {url}\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle", timeout=60000)
        time.sleep(2)

        tech = detect_technology(page)
        print(tech.summary())

        if tech.is_flutter:
            print("\nThis is Flutter Web, so it needs a special testing strategy.")
            print("See conftest.py for helper function usage.")
        else:
            print("\nThe page uses a standard DOM, so normal CSS selectors can be used.")

        print_comparison()
        browser.close()
