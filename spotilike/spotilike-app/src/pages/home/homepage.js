import React from "react";
import Artiste from "../artistes/artiste";
import AlbumsList from "../albums/albumsList";

function Home() {
  return (
    <div className="bg-[#121212] rounded-md h-full overflow-y-auto p-5">
      <Artiste />
      <AlbumsList />
    </div>
  );
}

export default Home;
