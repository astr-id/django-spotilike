import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const AlbumsList = () => {
  const [albums, setAlbums] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/albums/")
      .then((response) => setAlbums(response.data))
      .catch((error) =>
        console.error("Erreur lors du chargement des albums:", error)
      );
  }, []);

  return (
    <div className="bg-[#121212] text-white py-10 p-5">
      <div className="container">
        <h2 className="text-3xl font-bold mb-6 text-left">Albums</h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6">
          {albums.map((album) => (
            <Link
              to={`/albums/${album.id}`}
              key={album.id}
              className="group cursor-pointer"
            >
              <div className="p-5 hover:bg-[#1F1F1F] rounded-lg overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300">
                <img
                  src={
                    album.image ||
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/2024_Spotify_Logo.svg/1280px-2024_Spotify_Logo.svg.png"
                  }
                  alt={album.titre}
                  className="rounded-lg w-full h-full object-cover"
                />
                <div className="text-justify">
                  <h3 className="pt-1 text-lg font-semibold group-hover:underline">
                    {album.titre}
                  </h3>
                  <p className="pt-1 text-sm text-gray-400">
                    {album.artiste.nom}
                  </p>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AlbumsList;
