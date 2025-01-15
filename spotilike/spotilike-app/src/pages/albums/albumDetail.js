import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const AlbumDetail = () => {
  const { id } = useParams();
  const [album, setAlbum] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/albums/${id}/`)
      .then((response) => {
        setAlbum(response.data);
        setLoading(false);
      })
      .catch((error) =>
        console.error("Erreur lors du chargement de l'album:", error)
      );
  }, [id]);

  if (loading) {
    return <div className="text-white">Chargement...</div>;
  }

  if (!album) {
    return <div className="text-white">Album introuvable.</div>;
  }

  if (!album.morceaux || album.morceaux.length === 0) {
    return (
      <div className="text-white">Aucun morceau disponible pour cet album.</div>
    );
  }

  return (
    <div className="bg-[#121212] text-white min-h-screen">
      {/* Album Header */}
      <div className="flex flex-col md:flex-row items-end gap-6 p-8 md:p-16 bg-gradient-to-b from-green-800 to-[#121212]">
        <img
          src={
            album.image ||
            "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/2024_Spotify_Logo.svg/1280px-2024_Spotify_Logo.svg.png"
          }
          alt={album.titre}
          className="w-64 h-64 md:w-72 md:h-72 rounded-lg object-cover"
        />
        <div className="flex flex-col text-center md:text-left">
          <h2 className="text-sm font-bold uppercase text-white">Album</h2>
          <h1 className="text-5xl font-bold mt-2">{album.titre}</h1>
          <div className="flex items-center justify-center md:justify-start mt-4">
            <img
              src={album.artiste.avatar || "https://via.placeholder.com/50"}
              alt={album.artiste.nom}
              className="w-6 h-6 rounded-full object-cover mr-4"
            />
            <p className="text-lg text-gray-300 text-sm">
              <span className="text-white hover:underline">
                {album.artiste.nom}
              </span>{" "}
              • {new Date(album.date_sortie).getFullYear()} •{" "}
              {album.morceaux?.length || 0} titres
            </p>
          </div>
        </div>
      </div>

      {/* Section Morceaux  */}
      <div className="p-8">
        <table className="table-auto w-full text-left text-gray-300">
          <thead className="text-gray-500 border-b border-gray-700">
            <tr className="mt-2">
              <th className="w-8">#</th>
              <th className="py-2">Titre</th>
              <th className="w-20">Durée</th>
            </tr>
          </thead>
          <tbody>
            {album.morceaux?.map((morceau, index) => (
              <tr
                key={morceau.id}
                className="hover:bg-[#1F1F1F] transition-colors duration-300 text-gray-400"
              >
                <td className="py-3 rounded-l-lg">{index + 1}</td>
                <td className="py-3 font-bold text-white">{morceau.titre}</td>
                <td className="py-3 rounded-r-lg text-sm">{morceau.duree}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AlbumDetail;
