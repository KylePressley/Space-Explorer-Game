import React, { useState } from 'react';

function SolarSystemMap({ solarSystem, onPlanetClick }) {
  // ...
}

function PlanetInfoPanel({ planet }) {
  // ...
}

function PlayerStats({ player }) {
  // ...
}

function ActionButtons({ onHarvest, onMove, onInventory }) {
  // ...
}

function App() {
  const [solarSystem, setSolarSystem] = useState(generate_solar_system());
  const [currentPlanet, setCurrentPlanet] = useState(null);
  const [player, setPlayer] = useState(new Player());

  // ... game logic

  return (
    <div>
      <SolarSystemMap solarSystem={solarSystem} onPlanetClick={setCurrentPlanet} />
      <PlanetInfoPanel planet={currentPlanet} />
      <PlayerStats player={player} />
      <ActionButtons onHarvest={() => harvest_resources(player, solarSystem)}
                     onMove={() => move_to_next_planet(player, solarSystem)}
                     onInventory={() => display_inventory(player)} />
    </div>
  );
}