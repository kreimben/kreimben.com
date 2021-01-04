const DateParser = (date: string) => {

    const first = date.split('T');
    const second = first[1].split('.');
    const third = second[0].split(':');

    const _date = first[0];
    const time = third[0] + ':' + third[1];

    const result = new Array();

    result.push(_date);
    result.push(time);

    return result;
}

export default DateParser;