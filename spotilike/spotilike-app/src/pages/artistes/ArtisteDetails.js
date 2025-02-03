import React, { useEffect, useState } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import axios from "axios";

import { FaArrowLeft } from "react-icons/fa";

function ArtisteDetails() {
  const { id } = useParams(); // Récupération de l'ID de l'artiste depuis l'URL
  const navigate = useNavigate();
  const [artiste, setArtiste] = useState(null);
  const [albums, setAlbums] = useState([]);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/artists/${id}/`)
      .then((response) => {
        setArtiste(response.data);
      })
      .catch((error) => {
        console.error(
          "Erreur lors de la récupération des détails de l'artiste :",
          error
        );
      });
  }, [id]);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/albums/`)
      .then((response) => {
        const artistAlbums = response.data.filter(
          (album) => album.artiste === parseInt(id)
        );
        setAlbums(artistAlbums);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des albums :", error);
      });
  }, []);

  if (!artiste) {
    return <p>Chargement...</p>;
  }

  return (
    <div className="p-8 text-white h-full min-h-full overflow-x-auto">
      {console.log(albums)}
      <div className="flex flex-row items-center mb-6">
        {" "}
        {/* Flex Row pour aligner horizontalement */}
        <button
          onClick={() => navigate("/artistes")}
          className="text-white text-2xl hover:text-gray-300 mr-4"
        >
          <FaArrowLeft />
        </button>
        <h1 className="text-2xl font-bold">{artiste.nom}</h1>
      </div>
      <img
        src={artiste.avatar}
        alt={artiste.nom}
        className="w-[200px] h-[200px] rounded-full object-cover mb-4"
      />
      <p className="text-gray-400 mb-4">{artiste.biographie}</p>
      <h2 className="text-xl font-bold">Discographie</h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6">
        {albums.map((album) => (
          <Link
            to={`/albums/${album.id}`}
            key={album.id}
            className="group cursor-pointer"
          >
            <div className="p-5 hover:bg-[#1F1F1F] rounded-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
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
                  {new Date(album.date_sortie).getFullYear()}
                </p>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default ArtisteDetails;
