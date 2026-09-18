# Meow Cat

## Overview

Meow Cat is a cross-platform desktop utility that renders a persistent, interactive companion directly on your screen. Built with **Python** and **PyQt6**, it bypasses standard window constraints to float above all active applications, taskbars and full-screen windows.

The application utilizes pixel-perfect alpha masking to create a natural, frameless interaction zone, allowing you to drag the overlay across multiple virtual desktops and physical monitors without interrupting your workflow.

## Key Features

- **Absolute Top Z-Order**: Utilizes OS-level tooltip hints to aggressively maintain visibility over all other desktop elements.
- **Smart Monitor Tracking**: Continuously polls cursor position to calculate geometric proportions, automatically snapping the overlay to the active monitor.
- **Alpha-Channel Masking**: The physical clickable area is mapped precisely to the image's non-transparent pixels, allowing background clicks to pass through empty space.
- **Styled Context Menu**: A custom QSS-styled right-click menu for quick access to system controls and the integrated SQLite task manager.
