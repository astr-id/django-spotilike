import React, { useEffect, useState } from "react";
import axios from "axios";
import ArtisteCard from "./ArtisteCard";

function Artiste() {
  const [artistes, setArtistes] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/artists/")
      .then((response) => {
        setArtistes(response.data);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des artistes :", error);
      });
  }, []);

  return (
    <div className="bg-black min-h-screen p-8">
      <h1 className="text-white text-2xl font-bold mb-6">
        Artistes populaires
      </h1>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-6">
        {artistes.map((artiste) => (
          <ArtisteCard
            key={artiste.id}
            id={artiste.id}
            image={artiste.avatar}
            name={artiste.nom}
            role="Artiste"
          />
        ))}
      </div>
    </div>
  );
}

export default Artiste;
