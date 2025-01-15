import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./pages/home";
import Album from "./pages/albums";
import Artiste from "./pages/artistes";
function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/albums" element={<Album />} />
          <Route path="/artistes" element={<Artiste />} />
          {/* <Route path="/artistes/:id" element={<Artiste />} />
          <Route path="/albums/:id" element={<Artiste />} /> */}
          {/* Route pour les pages non trouvées */}
          {/* <Route path="*" element={<NotFound />} /> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
