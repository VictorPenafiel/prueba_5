from playwright.sync_api import Page, expect
import os

def test_actividades_page_navigation(page: Page):
    """
    This test verifies that a user can navigate from the main page
    to the Actividades Outdoor page by clicking the 'Actividades Outdoor' link.
    """
    # 1. Arrange: Go to the index.html page.
    # Use os.path.abspath to get the full path to the file
    page.goto(f"file://{os.path.abspath('index.html')}")

    # 2. Act: Find the "Actividades Outdoor" link and click it.
    actividades_link = page.get_by_role("link", name="Actividades Outdoor")
    actividades_link.click()

    # 3. Assert: Confirm the navigation was successful.
    # We expect the page title to be the same, but the h2 to be "Actividades Outdoor".
    expect(page.get_by_role("heading", name="Actividades Outdoor")).to_be_visible()

    # 4. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")