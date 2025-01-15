import React from "react";
import Artiste from "../artistes/artiste";

function Home() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Bienvenue sur Spotify</h1>
      <p className="text-gray-400">
        Explorez de la musique, des albums et plus encore.
      </p>
      <Artiste />
      {/* TODO : ajouter album */}
    </div>
  );
}

export default Home;
