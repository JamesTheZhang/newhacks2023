import React, { useState, useEffect } from 'react';
import { NavBar } from './Navbar.js';
import GMap from './maps.js';
//import jsonData from './data.json';
import {
  useJsApiLoader,
  GoogleMap,
  MarkerF,
  Autocomplete,
  InfoWindowF,
  DirectionsRenderer
} from '@react-google-maps/api';


export default function App() {
  

  console.log("loaded")
  return (
    <>
      <GMap friends={[
        { "name": "James", "latitude": 43.6764052278169045, "longitude": -79.39192191669248 },
        { "name": "Zach", "latitude": 43.664052278169045, "longitude": -79.39192191669248 },
        { "name": "Ryan", "latitude": 43.6564052278169045, "longitude": -79.39192191669248 }
      ]}
        groups={[
          { "building_name": "myhal", "latitude": 43.7564052278169045, "longitude": -79.33192191669248, "users": ["James", "Zach"] },
          { "building_name": "robarts", "latitude": 43.7749, "longitude": -79.389192191669248, "users": [] }
        ]} />
    </>
  )
}

