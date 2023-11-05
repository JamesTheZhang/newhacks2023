import React from 'react';
import {
  useJsApiLoader,
  GoogleMap,
  Marker,
  InfoWindowF,

} from '@react-google-maps/api';

const GMap = (props) => {
  const { isLoaded } = useJsApiLoader({
    googleMapsApiKey: process.env.NEXT_PUBLIC_API_KEY,
  })
  console.log(process.env.NEXT_PUBLIC_API_KEY)

  if (!isLoaded) {
    return <><div>
      LOADING
    </div></>
  }
  return (<GoogleMap
    zoom={12}
    center={{ lat: 43.664052278169045, lng: -79.39192191669248 }} // Set the default map center
    mapContainerStyle={{ height: "100vh", width: "100vw" }}
  >
    <Marker
      // key={friend.name}
      position={{ lat: 43.664052278169045, lng: -79 }}
    // icon="#"
    />
    {/* Display friends as distinct markers */}
    {props.friends.map(friend => {
      console.log(friend.latitude, friend.longitude)
      return (
        <Marker
          // key={friend.name}
          position={{ lat: friend.latitude, lng: friend.longitude }}
        // icon="#"
        />
      )
    })}

    {/* Display other users grouped by proximity */}
    {props.groups.map(group => (
      <Marker
        key={group.building_name}
        position={{ lat: group.latitude, lng: group.longitude }}
        label={`${group.users.length}`}
      />
    ))}
  </GoogleMap>)
}

export default GMap;
