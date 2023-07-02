/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{svelte,js,ts,css}'],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}