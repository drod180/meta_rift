import React, { PropTypes } from 'react'

const Champ = ({ onClick, imgURI, thumb }) => (
	<div onClick={onClick} className={thumb ? "thumb" : "full"}>
		<img src={imgURI} />
	</div>
)

export default Champ;
