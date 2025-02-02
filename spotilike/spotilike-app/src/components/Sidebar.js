import React from "react";
import { Link } from "react-router-dom";
import { FaUserAlt, FaMusic } from "react-icons/fa";

function Sidebar() {
  return (
    <div className="w-64 h-full m-3 p-3 shadow-lg flex flex-col items-center bg-[#121212] rounded-md">
      <ul className="w-full">
        <li className="flex bg-[#1F1F1F] items-center text-gray-300 mb-3 cursor-pointer hover:text-white hover:bg-gray-800 p-2 rounded-md transition-all duration-300">
          <Link to="/albums" className="flex items-center w-full">
            <FaMusic className="mr-4 text-lg" />
            <span>Albums</span>
          </Link>
        </li>
        <li className="flex bg-[#1F1F1F]  items-center text-gray-300 mb-6 cursor-pointer hover:text-white hover:bg-gray-800 p-2 rounded-md transition-all duration-300">
          <Link to="/artistes" className="flex items-center w-full">
            <FaUserAlt className="mr-4 text-lg" />
            <span>Artistes</span>
          </Link>
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
