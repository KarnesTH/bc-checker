function Navbar() {
  return (
    <>
      <nav className="bg-purple-600 shadow-lg">
        <div className="max-w-6xl mx-auto px-4">
          <div className="flex justify-between">
            <div className="flex space-x-7">
              <a href="#" className="flex items-center py-4">
                <span className="font-semibold text-orange-300 text-lg">
                  BC - Checker
                </span>
              </a>
            </div>
            <div className="hidden md:flex items-center space-x-1">
              <a
                href="#"
                className="py-4 px-2 text-blue-500 border-b-4 border-blue-500 font-semibold"
              >
                Dashboard
              </a>
            </div>
            <div className="md:hidden flex items-center">
              <button className="outline-none mobile-menu-button">
                <svg
                  className="w-6 h-6 text-gray-500"
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </nav>
    </>
  );
}

export default Navbar;
