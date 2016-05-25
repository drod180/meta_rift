import React, { PropTypes } from 'react'

const Details = ({ onClick, score, name }) => (
	<div>
		<p>{name}</p>
		<p>{score}</p>
	</div>
)

export default Details
