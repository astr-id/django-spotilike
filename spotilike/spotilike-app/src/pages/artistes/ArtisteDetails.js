import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";

import { FaArrowLeft } from "react-icons/fa";

function ArtisteDetails() {
  const { id } = useParams(); // Récupération de l'ID de l'artiste depuis l'URL
  const navigate = useNavigate();
  const [artiste, setArtiste] = useState(null);

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

  if (!artiste) {
    return <p>Chargement...</p>;
  }

  return (
    <div className="bg-black min-h-screen p-8 text-white">
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
    </div>
  );
}

export default ArtisteDetails;
