import React, { Component } from 'react'
import '../App.css';
import abnbLoading from '../assets/loadinganimation.gif';

export default class Loading extends Component {
  render() {
    return (
      <div>
        <img src={abnbLoading} alt=""/>
      </div>
    )
  }
}
