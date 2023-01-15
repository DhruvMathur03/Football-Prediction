import React, { useState, useEffect } from 'react';
import axios from 'axios';
import logo from './premier-league-logo.svg';
import './App.css';

function Prediction() {
    const [homeTeam, setHomeTeam] = useState('');
    const [awayTeam, setAwayTeam] = useState('');
    const [season, setSeason] = useState(0);
    const [homeGoalsProb, setHomeGoalsProb] = useState([]);
    const [awayGoalsProb, setAwayGoalsProb] = useState([]);

    const handleSubmit = event => {
      event.preventDefault(); 
      axios
        .get(`/prediction?home_team=${homeTeam}&away_team=${awayTeam}&season=${season}`)
        .then(res => {
          setHomeGoalsProb(res.data.home_goals_prob);
          setAwayGoalsProb(res.data.away_goals_prob);
        });
    }
    return (
        <div className='main'>
          <div className='header'>
            <img src={logo} className='App-logo'/>
            <div className='h1'>
              <h1>PREMIER LEAGUE SCORE PREDICTOR</h1>
            </div>
          </div>
          <hr style={{border: "1px solid #ccc"}} />
          <br />
          <br />
          <form onSubmit={handleSubmit} style={{display: "flex", justifyContent: "center"}}>
            <div style={{display: "flex", display: "flex", justifyContent: "space-between", width: "50%"}}>
              <label style={{textAlign: "center", width: "100%", position: "relative"}}>
                <span style={{position: "absolute", top: "-20px", left: "50%", transform: "translateX(-50%)"}}>
                  HOME
                </span>
                  <input type='text' style={{border: "none", borderBottom: "1px solid black"}} value={homeTeam} onChange={e => setHomeTeam(e.target.value)}/>
              </label>
              <br />
              <label style={{textAlign: "center", width: "100%", position: "relative"}}>
                <span style={{position: "absolute", top: "-20px", left: "50%", transform: "translateX(-50%)"}}> 
                  AWAY
                </span>
                  <input type='text' style={{border: "none", borderBottom: "1px solid black"}} value={awayTeam} onChange={e => setAwayTeam(e.target.value)}/>
              </label>
            </div>
            <br />
            <button type='submit'>
                Submit
            </button>
          </form>
          <br />
          <div>
            <h2>Home Team</h2>
            {homeGoalsProb.map((prob, index) => (
                <p key={index}>{`${index} goal(s): ${prob}%`}</p>
            ))}
          </div>
          <div>
            <h2>Away Team</h2>
            {awayGoalsProb.map((prob, index) => (
                <p key={index}>{`${index} goal(s): ${prob}%`}</p>
            ))}
          </div>
        </div>
    );
}

export default Prediction;