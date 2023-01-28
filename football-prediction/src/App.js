import React, { useState, useEffect } from 'react';
import axios from 'axios';
import logo from './premier-league-1.svg';
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

    const seasons = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022];

    return (
        <div className='main'>
          <div className='container'>
            <img src={logo} className='App-logo'/>
            <h1 className='h1'>PREMIER LEAGUE SCORE PREDICTOR</h1>
          </div>
          <hr className='line_under_header'/>
          <br />
          <br />
          <form onSubmit={handleSubmit} className='form1'>
            <div style={{display: "flex", display: "flex", justifyContent: "space-between", width: "50%"}}>
              <label className='label1'>
                <span className='span1'>
                  <h2>HOME</h2>
                </span>
                  <input type='text' className='input1' value={homeTeam} onChange={e => setHomeTeam(e.target.value)}/>
              </label>
              <br />
              <label className='label1'>
                <span className='span1'> 
                  <h2>AWAY</h2>
                </span>
                  <input type='text' className='input1' value={awayTeam} onChange={e => setAwayTeam(e.target.value)}/>
              </label>
            </div>
          </form>
          <br />
          <form onSubmit={handleSubmit}>
            <div>
              <label>
                Season :
                <div>
                  {seasons.map((year) => (<button key={year} onClick={() => setSeason(year)} className='season-button'> {year} </button>))}
                </div>
              </label>
            </div>
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