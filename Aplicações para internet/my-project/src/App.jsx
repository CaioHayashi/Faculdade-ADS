import BreakFast from "./components/BreakFast";
import Dinner from "./components/Dinner";
import Lunch from "./components/Lunch";
import Home from "./pages/Home";
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {
	return (
		<div>
			<BrowserRouter>
				<Home />
				<Routes>
					<Route path="/breakfast" element={<BreakFast />} />
					<Route path="/lunch" element={<Lunch />} />
					<Route path="/dinner" element={<Dinner />} />
				</Routes>
			</BrowserRouter>
		</div>
	);
}

export default App;
