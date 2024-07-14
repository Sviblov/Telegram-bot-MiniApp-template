import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import MiniApp from './MiniApp';

function HomePage() {
  const navigate = useNavigate();



  useEffect(() => {
    validateUser().then(userIsValid => {
      if (!userIsValid) {
        navigate('/notTelegram');
      }
    });
  }, [navigate]); 


  return (
    <div>
      <MiniApp />
    </div>
  );
}

function validateUser() {

  
  const debug = process.env.REACT_APP_DEBUG === 'true'
  
  if (debug) {
   
    return false; // For demonstration, always return false
  } else {
    
    const apiUrl = process.env.REACT_APP_API_URL + "/validation";
  
    // Making a synchronous API call using axios
    return axios.get(apiUrl, { userId: 'user123' }) // Replace with actual data
      .then(response => {
        return response.data.isValid;
      })
      .catch(error => {
        console.error('There was a problem with the axios operation:', error);
        return false;
      });


  }
}

export default HomePage;