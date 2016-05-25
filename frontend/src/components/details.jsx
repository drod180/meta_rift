import React, { PropTypes } from 'react'

export const Details = ({ onClick, score, name }) => (
	<div>
		<p>{name}</p>
		<p>{score}</p>
	</div>
)
