import { NavLink } from "react-router-dom";

const NavBar = () => {
	return (
		<nav className="flex justify-center gap-5 animate-fadeIn py-6 shadow-lg bg-slate-100">
			<NavLink end to="/breakfast">
				breakfast
			</NavLink>
			<NavLink to="/lunch" className='border-r-2 border-l-2 px-5'>lunch</NavLink>
			<NavLink to="/dinner">dinner</NavLink>
		</nav>
	);
};

export default NavBar;
