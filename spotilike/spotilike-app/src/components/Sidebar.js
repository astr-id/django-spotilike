import React from "react";
import { Link } from "react-router-dom";
import { FaHome, FaSearch, FaUserAlt, FaMusic } from "react-icons/fa";

function Sidebar() {
  return (
    <div className="w-64 bg-black p-4">
      <h1 className="text-2xl font-bold text-white mb-8">Spotify</h1>
      <ul>
        <li className="flex flex-col items-center text-gray-300 mb-6 cursor-pointer hover:text-white">
          <Link to="/">
            <FaHome className="mr-4" />
            Accueil
          </Link>
        </li>
        <li className="flex items-center text-gray-300 mb-6 cursor-pointer hover:text-white">
          <Link to="/albums">
            <FaMusic className="mr-4" />
            Albums
          </Link>
        </li>
        <li className="flex items-center text-gray-300 mb-6 cursor-pointer hover:text-white">
          <Link to="/artistes">
            <FaUserAlt className="mr-4" />
            Artistes
          </Link>
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
