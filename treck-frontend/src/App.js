import React, {useEffect, useState} from 'react'

const App = () => {
const [message, setMessage] = useState("");
const getIndex = async () =>{
    const requestOptions = {
    method: "GET",
    headers: {
        "Context-Type": "application/json",
        }
    };
    const response = await fetch("/", requestOptions);

    if(!response.ok){
    console.log("oh oh, something went wrong!");

    const data = response.json;
  }
}

  useEffect(() =>{
        getIndex();
    },[])
  return (
  <div><title>FishTrek</title></div>
  );
}

export default App;
