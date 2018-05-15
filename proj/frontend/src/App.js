import React, { Component } from 'react';

class App extends Component {
  state = {
    list: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/app/');
      const list = await res.json();
      this.setState({
        list
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.list.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
