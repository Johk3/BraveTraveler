import React from 'react';
// import { render } from '@testing-library/react';
import { shallow } from 'enzyme';
import App from './App';

describe('MyComponent', () => {
  it('should render correctly in "debug" mode', () => {    const component = shallow(<App debug />);
  
    expect(component).toMatchSnapshot();
  });
  it('should render correctly with no props', () => {
    const component = shallow(<App/>);

    expect(component.find("h1").text()).toContain("BraveTraveler - Monitoring")
  });
});
// test('renders learn react link', () => {
//   const { getByText } = render(<App />);
//   const linkElement = getByText(/learn react/i);
//   expect(linkElement).toBeInTheDocument();
// });
