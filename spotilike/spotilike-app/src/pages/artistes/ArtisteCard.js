import React from "react";
import { Link } from "react-router-dom";

function ArtisteCard({ image, name, role, id }) {
  return (
    <div className="flex flex-col items-center text-center">
      <img
        src={image}
        alt={name}
        className="w-[180px] h-[180px] rounded-full object-cover mb-2"
      />
      <Link
        to={`/artistes/${id}`}
        className="text-white text-lg font-semibold hover:underline"
      >
        {name}
      </Link>
      <p className="text-gray-400 text-sm">{role}</p>
    </div>
  );
}

export default ArtisteCard;
