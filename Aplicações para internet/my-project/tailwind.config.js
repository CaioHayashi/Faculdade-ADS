/** @type {import('tailwindcss').Config} */
export default {
	content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
	theme: { 
    fontFamily: {
      serif: ['Bodoni Moda', 'serif']
    },
		extend: {
			animation: {
				fadeIn: "fadeIn 1s ease"
			},
			keyframes: {
				fadeIn: {
					from: {
						opacity: "0",
						transform: "translateY(-20px)"
					},
					to: {
						opacity: "1",
						transform: "translateY(0)"
					}
				}
			}
		}
	},
	plugins: []
};
