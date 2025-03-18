# NetCtrl CMS Design System

This document outlines the design system for the NetCtrl CMS frontend, based on Material Design 3 (M3) principles. It provides guidance for maintaining visual consistency, accessibility, and usability across the application.

## Material Design 3 Foundation

Our design system follows Google's [Material Design 3](https://m3.material.io/foundations) (M3) principles which focus on:

- **Adaptable**: Works across all devices and platforms
- **Personal**: Dynamic theming based on user preferences
- **Accessible**: Inclusive design for all users

## Color System

### Primary Color Palette

Following M3's dynamic color system, we've implemented:

- **Primary**: #2196f3 (Blue)
- **Primary Light**: #64b5f6
- **Primary Dark**: #1976d2
- **Secondary**: #f50057 (Pink)
- **Secondary Light**: #ff4081
- **Secondary Dark**: #c51162

### Tonal Palette

Our design uses tonal variations based on the primary color:

- Surface colors
- Container colors
- Component-specific colors

### Themes

The application supports both light and dark themes with appropriate color adaptations:

#### Light Theme
- Background: #f5f5f5
- Surface: #ffffff
- On-Surface Text: rgba(0, 0, 0, 0.87)
- Secondary Text: rgba(0, 0, 0, 0.6)

#### Dark Theme
- Background: #121212
- Surface: #1e1e1e
- On-Surface Text: rgba(255, 255, 255, 0.87)
- Secondary Text: rgba(255, 255, 255, 0.6)

### Color Usage

- Use primary color for key actions and focus states
- Use secondary color for floating action buttons and selection controls
- Maintain adequate contrast ratios for text (4.5:1 for regular text)

## Typography

Following M3's type scale system:

| Role | Font | Weight | Size | Line Height |
|------|------|--------|------|------------|
| Display Large | Roboto | Regular | 57px | 64px |
| Display Medium | Roboto | Regular | 45px | 52px |
| Display Small | Roboto | Regular | 36px | 44px |
| Headline Large | Roboto | Regular | 32px | 40px |
| Headline Medium | Roboto | Regular | 28px | 36px |
| Headline Small | Roboto | Regular | 24px | 32px |
| Title Large | Roboto | Medium | 22px | 28px |
| Title Medium | Roboto | Medium | 16px | 24px |
| Title Small | Roboto | Medium | 14px | 20px |
| Body Large | Roboto | Regular | 16px | 24px |
| Body Medium | Roboto | Regular | 14px | 20px |
| Body Small | Roboto | Regular | 12px | 16px |

## Elevation

Following M3's elevation system to create a sense of depth and hierarchy:

| Level | Usage | Shadow |
|-------|-------|--------|
| 0 | Background elements | No shadow |
| 1 | Cards, surfaces | 0px 2px 1px -1px rgba(0,0,0,0.2) |
| 2 | Navigation drawers | 0px 3px 3px -2px rgba(0,0,0,0.2) |
| 3 | Navigation bar | 0px 3px 5px -1px rgba(0,0,0,0.2) |
| 4 | Dialogs | 0px 4px 5px -2px rgba(0,0,0,0.2) |
| 5 | Floating action buttons | 0px 6px 10px -3px rgba(0,0,0,0.2) |

## Shape

- **Component shape**: 4px border radius for components
- **Card shape**: 8px border radius
- **Button shape**: 4px border radius
- **Outline thickness**: 1px for normal state, 2px for focus state

## Components

### Buttons

- **Contained**: Filled with primary color, for primary actions
- **Outlined**: Border with transparent fill, for secondary actions
- **Text**: No border or fill, for tertiary actions

States:
- Normal
- Hover
- Focused
- Disabled

### Text Fields

- **Outlined**: Primary input style with visible border
- **Filled**: Alternative style with subtle background

States:
- Normal
- Focused
- Error
- Disabled

Input fields should have:
- Clear labels
- Helper text when needed
- Error states with informative messages
- Proper contrast for text input

### Cards

- **Elevated**: With shadow for content that can be interacted with
- **Outlined**: With border for static content
- **Filled**: With background color for grouping related content

### Navigation

- **Top App Bar**: App title, navigation menu, actions
- **Navigation Drawer**: Primary navigation destinations
- **Bottom Navigation**: Alternative for mobile devices

## Motion

Apply meaningful motion that guides users through their journey:

- **Standard curve**: For most transitions (ease)
- **Deceleration curve**: For elements entering the screen
- **Acceleration curve**: For elements leaving the screen
- **Sharp curve**: For elements that quickly expand or contract

## Accessibility Guidelines

- **Text contrast**: Minimum 4.5:1 for regular text, 3:1 for large text
- **Target size**: Interactive elements should be at least 44×44dp
- **Focus indicators**: Clear visual indicators for keyboard navigation
- **Screen reader support**: All elements should have appropriate ARIA attributes
- **Keyboard navigation**: All functionality available via keyboard

## Responsive Design

Our application adapts to different screen sizes:

- **Small** (< 600dp): Single column layout, stacked elements
- **Medium** (600dp - 840dp): Two column layout
- **Large** (> 840dp): Multi-column layout

## Implementation Details

Our implementation uses Material UI components with customized themes to match Material Design 3 principles. The theme configuration in `ThemeContext.tsx` defines colors, typography, component styles, and dark/light theme support.

### Example Theme Configuration

```typescript
const theme = createTheme({
  palette: {
    mode,
    primary: {
      main: '#2196f3',
      light: '#64b5f6',
      dark: '#1976d2',
    },
    // Additional configuration...
  },
  typography: {
    fontFamily: ['"Roboto"', 'Arial', 'sans-serif'].join(','),
    // Type scale configuration...
  },
  // Components styling...
});
```

## Resources

- [Material Design 3 Guidelines](https://m3.material.io/)
- [Material UI Documentation](https://mui.com/material-ui/)
- [Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/)
