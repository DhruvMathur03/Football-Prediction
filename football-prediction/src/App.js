import React, { useState, useEffect } from 'react';
import axios from 'axios';

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
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Home Team :
                    <input type='text' value={homeTeam} onChange={e => setHomeTeam(e.target.value)}/>
                </label>
                <br />
                <label>
                    Away Team :
                    <input type='text' value={awayTeam} onChange={e => setAwayTeam(e.target.value)}/>
                </label>
                <br />
                <label>
                    Season :
                    <input type='number' value={season} onChange={e => setSeason(e.target.value)}/>
                </label>
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