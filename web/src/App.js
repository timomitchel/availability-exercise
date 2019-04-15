import React, { Component } from 'react';
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      available_times: {},
      instructor_keys: [],
    }
  }

  componentDidMount(){
    this.fetchAvailableTimes();
  }

  async fetchAvailableTimes() {
    try {
      const res = await fetch("http://localhost:4433/available_times");
      const json = await res.json();
      this.setState({available_times: json.available_times});
      var isDisabled = this.state.name === ""
    } catch (e) {
      console.error("Failed to fetch 'available_times' data", e);
    }
    this.getKeys()
  }

  getKeys = () => {
    const availableTimes = this.state.available_times
    const availableKeys = Object.keys(availableTimes)
    this.setState({
      name: "",
      instructor_keys: availableKeys
    })
  }

  displayTimes = () => {
    if (this.state.available_times){
      return this.state.available_times;
    }
  }

  handleChange = (e) => {
    this.setState({ name: e.target.value })
  }

  render() {
    return (
      <div className="App container">
      <h1>Book Time with an Advisor</h1>

        <form id="name-form" className="col-md-6">
          <div className="form-group">
            <label htmlFor="name-field">Your Name</label>
            <input value={this.state.name} onChange={this.handleChange} type="text" id="name-field" className="form-control" placeholder="Enter Name"/>
          </div>
        </form>
        <h2>Available Times</h2>
      <InstructorKeys availableTimes={this.state.available_times}/>
      </div>
    );
  }
}
class InstructorKeys extends Component {
  render() {
    return (
      <table className="advisors table">
        <thead>
          <tr>
            <th>Advisor ID</th>
            <th>Available Times</th>
          </tr>
        </thead>
      <tbody>
        {
          Object.entries(this.props.availableTimes).map(([key, value], j) => (
              <tr>
                <td>{key}</td>
                <td>
                  <ul>
                    <li>
                      {value.map(time =>
                      <div>
                        <time dateTime={time} className="book-time">{time}</time>
                        <button disabled={this.isDisabled} className="book btn-small btn-primary">Book</button>
                      </div>
                      )}
                    </li>
                  </ul>
                </td>
              </tr>
          ))
        }
        </tbody>
      </table>
    );
  }
}
export default App;

