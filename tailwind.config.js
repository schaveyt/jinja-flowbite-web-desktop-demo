/** @type {import('tailwindcss').Config} */
module.exports = {
  
  content: [
    "./my_app/templates/**/*.{html,jinja}",
    "./my_app/static/js/**/*.js",
    "./node_modules/flowbite/**/*.js",
    "./venv/Lib/site-packages/jinja_flowbite/**/*.{html,jinja}"

  ],
  darkMode: 'class',
  theme: {
      extend: {
          colors: {
              primary: { "50": "#eff6ff", "100": "#dbeafe", "200": "#bfdbfe", "300": "#93c5fd", "400": "#60a5fa", "500": "#3b82f6", "600": "#2563eb", "700": "#1d4ed8", "800": "#1e40af", "900": "#1e3a8a", "950": "#172554" }
          },
          maxHeight: {
              'table-xl': '60rem',
          }
      },
      fontFamily: {
          'body': [
              'Inter',
              'ui-sans-serif',
              'system-ui',
              '-apple-system',
              'system-ui',
              'Segoe UI',
              'Roboto',
              'Helvetica Neue',
              'Arial',
              'Noto Sans',
              'sans-serif',
              'Apple Color Emoji',
              'Segoe UI Emoji',
              'Segoe UI Symbol',
              'Noto Color Emoji'
          ],
          'sans': [
              'Inter',
              'ui-sans-serif',
              'system-ui',
              '-apple-system',
              'system-ui',
              'Segoe UI',
              'Roboto',
              'Helvetica Neue',
              'Arial',
              'Noto Sans',
              'sans-serif',
              'Apple Color Emoji',
              'Segoe UI Emoji',
              'Segoe UI Symbol',
              'Noto Color Emoji'
          ],
          'mono': [
            'ui-monospace',
            'SFMono-Regular',
            'MesloLGL Nerd Font Mono', 
            'Cascadia Mono',
            'Courier New'
        ]
      }
  },
  safelist: [
      {
          pattern: /^(fill-)/, // This is to support dynamically generated fill color for the spinner.
          // variants: ["hover", "active", "dark", "dialog"],
      },
  ],
  plugins: [
      require('flowbite/plugin')
  ],
}