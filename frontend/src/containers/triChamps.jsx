import React, { Component } from 'react';
import Champ from '../components/champ';
import Details from '../components/details';


export default class TriChamps extends Component {
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
          imgURI={"./images/test_thumb.png"}
          thumb
        />
        <Details
          onClick={this.detailClick}
          name={"Champ-1"}
          score={84}
        />
        <Champ
          onClick={this.champClick}
          imgURI={"./images/test_thumb.png"}
          thumb
        />
        <Details
          onClick={this.detailClick}
          name={"Champ-2"}
          score={82}
        />
        <Champ
          onClick={this.champClick}
          imgURI={"./images/test_thumb.png"}
          thumb
        />
        <Details
          onClick={this.detailClick}
          name={"Champ-3"}
          score={80}
        />
      </div>
    );
  }
}
