# Accessibility Guide for NetCtrl CMS Frontend

This guide outlines the accessibility standards implemented in the NetCtrl CMS frontend to ensure proper visual accessibility and compliance with WCAG (Web Content Accessibility Guidelines) standards.

## Implemented Accessibility Features

### Color Contrast

- **Text on Background**: We maintain a minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text.
- **Input Fields**: All input fields have been configured to ensure text remains visible in both light and dark modes.
- **Links and Interactive Elements**: Links and interactive elements have sufficient contrast against their backgrounds.

### Theme Support

- **Light/Dark Mode**: The application supports both light and dark mode with appropriate color adjustments for each.
- **System Preference Detection**: The theme automatically detects system preferences for light/dark mode.
- **Manual Toggle**: Users can manually toggle between modes.

### Form Elements

- **Input Focus States**: Enhanced focus states on form elements to make them more visible.
- **Label Visibility**: Form labels are styled for better visibility.
- **Error States**: Form validation errors are clearly indicated with descriptive text.

## Accessibility Development Guidelines

When developing new components or modifying existing ones, please follow these guidelines:

### Text and Colors

1. **Text Contrast**:
   - Regular text: Minimum 4.5:1 contrast ratio against the background
   - Large text (18pt+): Minimum 3:1 contrast ratio against the background
   - Use the built-in theme text colors: `theme.palette.text.primary` and `theme.palette.text.secondary`

2. **Color Usage**:
   - Never use color as the only means to convey information
   - Ensure all interactive elements have visual cues beyond color
   - Test your components in both light and dark modes

### Form Components

1. **Input Fields**:
   - Ensure text is visible with appropriate contrast
   - Maintain clear focus states
   - Associate labels with form controls using `htmlFor`
   - Provide clear validation error messages

2. **Interactive Elements**:
   - Ensure buttons and clickable elements have:
     - Sufficient size (minimum touch target of 44x44px for mobile)
     - Clear hover and focus states
     - Descriptive text or aria-labels

### Navigation and Structure

1. **Keyboard Navigation**:
   - Ensure all interactive elements are keyboard accessible
   - Maintain a logical tab order
   - Provide visible focus indicators

2. **Semantic HTML**:
   - Use appropriate HTML elements (`<button>`, `<a>`, `<input>`, etc.)
   - Use heading levels (`<h1>` through `<h6>`) to create a clear document outline
   - Group related form elements with `<fieldset>` and `<legend>`

## Testing Accessibility

Before submitting changes, test your components for:

1. **Keyboard Navigation**: Can you operate all functions using only the keyboard?
2. **Screen Reader Compatibility**: Do all elements provide appropriate context?
3. **Color Contrast**: Does all text meet the minimum contrast requirements?
4. **Resizing**: Does the interface work when text is resized up to 200%?
5. **Mode Testing**: Test in both light and dark modes.

## Accessibility Testing Tools

- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- [axe DevTools](https://www.deque.com/axe/)
- [Contrast Checker](https://webaim.org/resources/contrastchecker/)
- Built-in browser tools (Chrome Lighthouse, Firefox Accessibility Inspector)

## Resources

- [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/)
- [Material UI Accessibility](https://mui.com/material-ui/guides/accessibility/)
- [React Accessibility](https://reactjs.org/docs/accessibility.html)
