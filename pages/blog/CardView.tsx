import Link from 'next/link';

type blogParams = { title: string, date: Date };

const CardView: React.FunctionComponent<blogParams> = ({ title, date }) => (
    <div className="bg-gray-500" >
        <p className="text-red-700 text-lg" > title: {title} </p>
        < p > date: {date} </p>
    </div>
);