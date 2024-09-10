if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    // Apply dark skin and content_css
    tinymce.init({
        ...
        skin: 'oxide-dark',
        content_css: '/path/to/dark/theme.css',
        ...
    });
} else {
    // Apply default skin and content_css
    tinymce.init({
        ...
        skin: 'default',
        content_css: '/path/to/light/theme.css',
        ...
    });
}