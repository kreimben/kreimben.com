
export default function CardView( { title, date } ) {

    console.log(title);
    console.log(date);

    return (
        <div className="bg-gray-500">
            <p className="text-red-700 text-lg">title: {title}</p>
            <p>date: {date}</p>
        </div>
    );
}