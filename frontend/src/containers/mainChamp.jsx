import React, { Component } from 'react';
import Champ from '../components/champ';
import Details from '../components/details';


export default class MainChamp extends Component {
  constructor(props) {
    super(props);
    this.champClick = this.champClick.bind(this);
    this.detailClick = this.detailClick.bind(this);
  }

  champClick(e) {
    e.preventDefault();
  }

  detailClick(e) {
    e.preventDefault();
  }

  render() {
    return (
      <div>
        <Champ
          onClick={this.champClick}
          imgURI={"./images/test_full.jpg"}
          thumb={false}
        />
        <Details
          onClick={this.detailClick}
          name={"Fiora"}
          score={85}
        />
      </div>
    );
  }
}
