import React, { Component } from 'react';
import Loading from './components/Loading.js';
import './App.css';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true
    };
  }

  componentDidMount() {
    setTimeout(() => this.setState({ loading: false }), 2000)
  }

  render() {
    return (
      <div className="App">
        {/* <h1>Hello</h1> */}
        { (this.state.loading) ? <Loading/> : "" }
      </div>
    )
  };
}
