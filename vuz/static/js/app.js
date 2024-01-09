function App() {
    const [likes, setLikes] = React.useState(0)
    function inc() {
        setLikes(likes+1)
    }
    function dec() {
        setLikes(likes-1)
    }
    return (
        <div>
            <h1>{likes}</h1>
            <button onClick={inc}>Inc</button>
            <button onClick={dec}>Dec</button>
        </div>
    );
}