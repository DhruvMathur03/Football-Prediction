import React, { useState, useEffect } from 'react';
import axios from 'axios';
import logo from './premier-league-logo.svg';
import arsenal from "./premier-league/arsenal.png"
import aston_villa from "./premier-league/aston-villa.png"
import bournemouth from "./premier-league/bournemouth.png"
import brentford from "./premier-league/brentford.png"
import brighton from "./premier-league/brighton.png"
import burnley from "./premier-league/burnley.png"
import cardiff_city from "./premier-league/cardiff-city.png"
import chelsea from "./premier-league/chelsea.png"
import crystal_palace from "./premier-league/crystal-palace.png"
import everton from "./premier-league/everton.png"
import fulham from "./premier-league/fulham.png"
import huddersfield_town from "./premier-league/hudderfield-town.png"
import hull_city from "./premier-league/hull-city.png"
import leeds_united from "./premier-league/leeds-united.png"
import leicester_city from "./premier-league/leicester-city.png"
import liverpool from "./premier-league/liverpool.png"
import manchester_city from "./premier-league/manchester-city.png"
import manchester_united from "./premier-league/manchester-united.png"
import middlesborough from "./premier-league/middlesbrough.png"
import newcastle_united from "./premier-league/newcastle-united.png"
import norwich_city from "./premier-league/norwich-city.png"
import queens_park_rangers from "./premier-league/queens-park-rangers.png"
import reading from "./premier-league/reading.png"
import sheffield_united from "./premier-league/sheffield-united.png"
import southampton from "./premier-league/southampton.png"
import stoke_city from "./premier-league/stoke-city.png"
import sunderland from "./premier-league/sunderland.png"
import swansea_city from "./premier-league/swansea-city.png"
import tottenham_hotspur from "./premier-league/tottenham-hotspur.png"
import watford from "./premier-league/watford.png"
import west_bromwich_albion from "./premier-league/west-bromwich-albion.png"
import west_ham_united from "./premier-league/west-ham-united.png"
import wigan_athletic from "./premier-league/wigan-athletic.png"
import wolves from "./premier-league/wolves.png"
import './App.css';

function Prediction() {
    const [homeTeam, setHomeTeam] = useState('');
    const [awayTeam, setAwayTeam] = useState('');
    const [season, setSeason] = useState(0);
    const [homeGoalsProb, setHomeGoalsProb] = useState([]);
    const [awayGoalsProb, setAwayGoalsProb] = useState([]);
    const [hoveredSeason, setHoveredSeason] = useState(0);

    const handleSubmit = event => {
      event.preventDefault(); 
      axios
        .get(`/prediction?home_team=${homeTeam}&away_team=${awayTeam}&season=${season}`)
        .then(res => {
          setHomeGoalsProb(res.data.home_goals_prob);
          setAwayGoalsProb(res.data.away_goals_prob);
        });
    }

    const handleSeasonMouseOver = year => {
      setHoveredSeason(year);
    };
      
    const handleSeasonMouseOut = () => {
      setHoveredSeason(0);
    };
    const teams = {
      "arsenal" : arsenal,
      "aston villa" : aston_villa,
      "bournemouth" : bournemouth,
      "brentford" : brentford,
      "brighton" : brighton,
      "burnley" : burnley,
      "cardiff city" : cardiff_city,
      "chelsea" : chelsea,
      "crystal palace" : crystal_palace,
      "everton" : everton,
      "fulham" : fulham,
      "huddersfield town" : huddersfield_town,
      "hull city" : hull_city,
      "leeds united" : leeds_united,
      "leicester city" : leicester_city,
      "liverpool" : liverpool,
      "manchester city" : manchester_city,
      "manchester united" : manchester_united,
      "middlesbrough" : middlesborough,
      "newcastle united" : newcastle_united,
      "norwich city" : norwich_city,
      "queens park rangers" : queens_park_rangers,
      "reading" : reading,
      "sheffield united" : sheffield_united,
      "southampton" : southampton,
      "stoke city" : stoke_city,
      "sunderland" : sunderland,
      "swansea city" : swansea_city,
      "tottenham hotspur" : tottenham_hotspur,
      "watford" : watford,
      "west bromwich albion" : west_bromwich_albion,
      "west ham united" : west_ham_united,
      "wigan athletic" : wigan_athletic,
      "wolves" : wolves
    }
  

    const seasons = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022];

    return (
        <div className='main'>
          <div className='container'>
            <img src={logo} className='App-logo'/>
            <h1 className='h1'>PREMIER LEAGUE SCORE PREDICTOR</h1>
          </div>

          <br />
          <br />
          <form onSubmit={handleSubmit} className='form1'>
            <div style={{display: "flex", justifyContent: "space-between", width: "50%"}}>
              <label className='label1'>
                <span className='span1'>
                  <h2 className='font'>HOME</h2>
                </span>
                  <input type='text' className='input1' value={homeTeam} onChange={e => setHomeTeam(e.target.value)}/>
              </label>
              <br />
              <label className='label1'>
                <span className='span1'> 
                  <h2 className='font'>AWAY</h2>
                </span>
                  <input type='text' className='input1' value={awayTeam} onChange={e => setAwayTeam(e.target.value)}/>
              </label>
            </div>
          </form>
          <div className='logos'>
            {homeTeam !== '' && <img src={teams[Object.keys(teams).filter((key) => key.includes(homeTeam.toLowerCase()))]}
                 className='team-logo'/>}
            {awayTeam !== '' && <img src={teams[Object.keys(teams).filter((key) => key.includes(awayTeam.toLowerCase()))]}
                 className='team-logo'/>}
          </div>
          <br />
          <div>
            <label>
              <h3 className='font'>SEASON</h3>
              <div>
                {seasons.map((year) => (<button key={year} 
                onMouseOver={() => handleSeasonMouseOver(year)}
                onMouseOut={handleSeasonMouseOut}
                onClick={() => setSeason(year)}
                className={`season-button ${setSeason === year|| hoveredSeason === year ? 'hovered' : ''}`}> {year} </button>))}
              </div>
            </label>
          </div>
          <br />
          <form onSubmit={handleSubmit}>
            <button type='submit' className='finalPredict'>PREDICT</button>
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