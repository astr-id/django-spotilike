import React from "react";
import logo from "../assets/logoSpotilike.png";
import { GoHomeFill } from "react-icons/go";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header className="flex items-center p-4 bg-black">
      <img src={logo} alt="logo" className="h-10 mr-2" />
      <span className="text-white text-2xl font-bold mr-5">Spotilike</span>
      <div className="flex items-center">
        <Link
          to="/"
          className="text-white text-lg p-2 rounded-full bg-[#1F1F1F]"
        >
          <GoHomeFill className="text-white text-3xl" />
        </Link>
      </div>
    </header>
  );
};

export default Header;
