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
    <div className="bg-[#121212] text-white py-10 p-5">
      <div className="container">
        <h2 className="text-3xl font-bold mb-6 text-left">Albums</h2>
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
    </div>
  );
}

export default Artiste;
