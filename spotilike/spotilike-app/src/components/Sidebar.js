import React from "react";
import { Link } from "react-router-dom";
import { FaHome, FaUserAlt, FaMusic } from "react-icons/fa";
import image from "../assets/logoSpotilike.png";

function Sidebar() {
  return (
    <div className="w-64 bg-black p-6 shadow-lg flex flex-col items-center">
      <img
        src={image}
        alt="Logo"
        className="w-32 mb-8 object-contain"
      />

      <h1 className="text-3xl font-bold text-white mb-8">Spotilike</h1>

      <ul className="w-full">
        <li className="flex items-center text-gray-300 mb-6 cursor-pointer hover:text-white hover:bg-gray-800 p-2 rounded-md transition-all duration-300">
          <Link to="/" className="flex items-center w-full">
            <FaHome className="mr-4 text-lg" />
            <span>Accueil</span>
          </Link>
        </li>
        <li className="flex items-center text-gray-300 mb-6 cursor-pointer hover:text-white hover:bg-gray-800 p-2 rounded-md transition-all duration-300">
          <Link to="/albums" className="flex items-center w-full">
            <FaMusic className="mr-4 text-lg" />
            <span>Albums</span>
          </Link>
        </li>
        <li className="flex items-center text-gray-300 mb-6 cursor-pointer hover:text-white hover:bg-gray-800 p-2 rounded-md transition-all duration-300">
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
