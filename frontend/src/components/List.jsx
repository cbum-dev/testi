function List(props){
    function handleClick(){
  props.deletion(props.id)
}
  return (
      <div className="note">
        <h1 >  Titles: {props.name} </h1>
        <p > Content: {props.age}</p>
        <button onClick={handleClick}>Deleted</button>
      </div>
  )
}

export default List;
