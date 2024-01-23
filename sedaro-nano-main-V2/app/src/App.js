import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';

/**
 * UPDATE
 * Wrapped parts of the code into functions to make it easier to read.
 */

const App = () => {
  // Store plot data in state.
  const [plotData, setPlotData] = useState([]);

  useEffect(() => {
    // fetch plot data when the component mounts

    async function fetchData() {
      console.log('calling fetchdata...');

      try {
        // 'data.json' should be populated from a run of sim.py
        const response = await fetch('data.json');
        const data = await response.json();
        const updatedPlotData = {};

        data.forEach(([t0, t1, frame]) => {
          for (let [agentId, { x, y }] of Object.entries(frame)) {
            updatedPlotData[agentId] = updatedPlotData[agentId] || { x: [], y: [] };
            updatedPlotData[agentId].x.push(x);
            updatedPlotData[agentId].y.push(y);
          }
        });

        setPlotData(Object.values(updatedPlotData));
        console.log('plotData:', Object.values(updatedPlotData));
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
  }, []);

  function update () 
    {
      var style = {
        position: 'fixed', width: '100%', height: '100%', left: 0, top: 0 
      }
      var layout = {
        title: 'Visualization',
        yaxis: { scaleanchor: 'x' },
        autosize: true,
      }
      return <Plot
      style={style}
      data={plotData}
      layout={layout}
      />
    }

  return (update());
};

export default App;
