use crate::business_days::*;
use crate::sub::*;
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use serde::Deserialize;

#[derive(Deserialize)]
pub struct BusinessDayKwargs {
    holidays: Vec<i32>,
    weekmask: [bool; 7],
}

fn bday_output(input_fields: &[Field]) -> PolarsResult<Field> {
    let field = input_fields[0].clone();
    Ok(field)
}

#[polars_expr(output_type_func=bday_output)]
fn advance_n_days(inputs: &[Series], kwargs: BusinessDayKwargs) -> PolarsResult<Series> {
    let s = &inputs[0];
    let n = &inputs[1].cast(&DataType::Int32)?;
    let weekmask = kwargs.weekmask;
    let holidays = kwargs.holidays;

    impl_advance_n_days(s, n, holidays, &weekmask)
}

#[polars_expr(output_type=Int32)]
fn sub(inputs: &[Series], kwargs: BusinessDayKwargs) -> PolarsResult<Series> {
    let begin_dates = &inputs[0];
    let end_dates = &inputs[1];
    let weekmask = kwargs.weekmask;
    let holidays = kwargs.holidays;
    impl_sub(begin_dates, end_dates, &weekmask, &holidays)
}
