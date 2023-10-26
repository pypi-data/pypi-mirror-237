#include "lib.h"

namespace qlat
{  //

template <class M>
PyObject* mk_spfield_ctype(int dummy)
{
  (void)dummy;
  SelectedPoints<M>* pspfield = new SelectedPoints<M>();
  return py_convert((void*)pspfield);
}

template <class M>
PyObject* mk_spfield_psel_ctype(const PointsSelection& psel, const int multiplicity)
{
  SelectedPoints<M>* pspfield = new SelectedPoints<M>();
  SelectedPoints<M>& spfield = *pspfield;
  spfield.init(psel, multiplicity);
  return py_convert((void*)pspfield);
}

template <class M>
PyObject* free_spfield_ctype(PyField& pf)
{
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  delete &f;
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_spfield_ctype(PyField& pf_new, PyField& pf)
{
  SelectedPoints<M>& f_new = *(SelectedPoints<M>*)pf_new.cdata;
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  f_new = f;
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_spfield_field_ctype(PyField& pspf, PyField& pf,
                                 const PointsSelection& psel)
{
  SelectedPoints<M>& sp = *(SelectedPoints<M>*)pspf.cdata;
  const Field<M>& f = *(Field<M>*)pf.cdata;
  set_selected_points(sp, f, psel);
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_spfield_sfield_ctype(PyField& pspf, PyField& psf,
                                   const PointsSelection& psel,
                                   const FieldSelection& fsel)
{
  SelectedPoints<M>& sp = *(SelectedPoints<M>*)pspf.cdata;
  const SelectedField<M>& sf = *(SelectedField<M>*)psf.cdata;
  set_selected_points(sp, sf, psel, fsel);
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_field_spfield_ctype(PyField& pf, PyField& pspf,
                                  const PointsSelection& psel)
{
  Field<M>& f = *(Field<M>*)pf.cdata;
  const SelectedPoints<M>& sp = *(SelectedPoints<M>*)pspf.cdata;
  set_field_selected(f, sp, f.geo(), psel);
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_sfield_spfield_ctype(PyObject* p_sfield, PyObject* p_spfield,
                                   const FieldSelection& fsel,
                                   const PointsSelection& psel)
{
  SelectedField<M>& sf = py_convert_type_sfield<M>(p_sfield);
  const SelectedPoints<M>& sp = py_convert_type_spoints<M>(p_spfield);
  set_selected_field(sf, sp, fsel, psel);
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_add_spfield_ctype(PyField& pf_new, PyField& pf)
{
  SelectedPoints<M>& f_new = *(SelectedPoints<M>*)pf_new.cdata;
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  f_new += f;
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_sub_spfield_ctype(PyField& pf_new, PyField& pf)
{
  SelectedPoints<M>& f_new = *(SelectedPoints<M>*)pf_new.cdata;
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  f_new -= f;
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_mul_spfield_ctype(PyField& pf, const Complex& factor)
{
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  f *= factor;
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_mul_spfield_ctype(PyField& pf, const double& factor)
{
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  f *= factor;
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_zero_spfield_ctype(PyField& pf)
{
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  set_zero(f);
  Py_RETURN_NONE;
}

template <class M>
PyObject* acc_field_spfield_ctype(PyObject* p_field, PyObject* p_spfield,
                                  const PointsSelection& psel)
{
  Field<M>& f = py_convert_type_field<M>(p_field);
  const SelectedPoints<M>& sp = py_convert_type_spoints<M>(p_spfield);
  acc_field(f, sp, f.geo(), psel);
  Py_RETURN_NONE;
}

template <class M>
PyObject* get_n_points_spfield_ctype(PyField& pf)
{
  SelectedPoints<M>& spf = *(SelectedPoints<M>*)pf.cdata;
  const long ret = spf.n_points;
  return py_convert(ret);
}

template <class M>
PyObject* get_multiplicity_spfield_ctype(PyField& pf)
{
  SelectedPoints<M>& spf = *(SelectedPoints<M>*)pf.cdata;
  const long ret = spf.multiplicity;
  return py_convert(ret);
}

template <class M>
PyObject* qnorm_spfield_ctype(PyField& pf)
{
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  const double ret = qnorm(f);
  return py_convert(ret);
}

template <class M>
PyObject* qnorm_field_spfield_ctype(SelectedPoints<double>& f, PyObject* p_field1)
{
  const SelectedPoints<M>& f1 = py_convert_type_spoints<M>(p_field1);
  qnorm_field(f, f1);
  Py_RETURN_NONE;
}

template <class M>
PyObject* get_elems_spfield_ctype(PyField& pf, const long idx)
{
  const SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  return py_convert(f.get_elems_const(idx));
}

template <class M>
PyObject* get_elem_spfield_ctype(PyField& pf, const long idx, const int m)
{
  const SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  if (m >= 0) {
    return py_convert(f.get_elem(idx, m));
  } else {
    return py_convert(f.get_elem(idx));
  }
}

template <class M>
PyObject* set_elems_spfield_ctype(PyObject* p_field, const long idx,
                                  PyObject* p_val)
{
  SelectedPoints<M>& f = py_convert_type_spoints<M>(p_field);
  const int multiplicity = f.multiplicity;
  qassert((long)PyBytes_Size(p_val) == (long)multiplicity * (long)sizeof(M));
  const Vector<M> val((M*)PyBytes_AsString(p_val), multiplicity);
  assign(f.get_elems(idx), val);
  Py_RETURN_NONE;
}

template <class M>
PyObject* set_elem_spfield_ctype(PyObject* p_field, const long idx,
                                const int m, PyObject* p_val)
{
  SelectedPoints<M>& f = py_convert_type_spoints<M>(p_field);
  qassert(PyBytes_Size(p_val) == sizeof(M));
  const M& val = *(M*)PyBytes_AsString(p_val);
  f.get_elem(idx, m) = val;
  Py_RETURN_NONE;
}

template <class M>
PyObject* save_complex_spfield_ctype(PyField& pf, const std::string& path)
{
  const SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  save_selected_points_complex(f, path);
  Py_RETURN_NONE;
}

template <class M>
PyObject* load_complex_spfield_ctype(PyField& pf, const std::string& path)
{
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  load_selected_points_complex(f, path);
  Py_RETURN_NONE;
}

template <class M>
PyObject* lat_data_from_complex_spfield_ctype(LatData& ld, PyField& pf)
{
  const SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  ld = lat_data_from_selected_points_complex(f);
  Py_RETURN_NONE;
}

template <class M>
PyObject* complex_spfield_from_lat_data_ctype(PyField& pf, const LatData& ld)
{
  SelectedPoints<M>& f = *(SelectedPoints<M>*)pf.cdata;
  selected_points_from_lat_data_complex(f, ld);
  Py_RETURN_NONE;
}

}  // namespace qlat

EXPORT(set_add_spfield, {
  using namespace qlat;
  PyObject* p_field_new = NULL;
  PyObject* p_field = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_field_new, &p_field)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  qassert(ctype == py_get_ctype(p_field_new));
  PyField pf_new = py_convert_field(p_field_new);
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, set_add_spfield_ctype, ctype, pf_new, pf);
  return p_ret;
})

EXPORT(set_sub_spfield, {
  using namespace qlat;
  PyObject* p_field_new = NULL;
  PyObject* p_field = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_field_new, &p_field)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  qassert(ctype == py_get_ctype(p_field_new));
  PyField pf_new = py_convert_field(p_field_new);
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, set_sub_spfield_ctype, ctype, pf_new, pf);
  return p_ret;
})

EXPORT(set_mul_double_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  double factor = 0.0;
  if (!PyArg_ParseTuple(args, "Od", &p_field, &factor)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, set_mul_spfield_ctype, ctype, pf, factor);
  return p_ret;
})

EXPORT(set_zero_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  if (!PyArg_ParseTuple(args, "O", &p_field)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, set_zero_spfield_ctype, ctype, pf);
  return p_ret;
})

EXPORT(acc_field_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  PyObject* p_spfield = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_field, &p_spfield)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_spfield);
  qassert(ctype == py_get_ctype(p_field));
  const PointsSelection& psel = py_convert_type<PointsSelection>(p_spfield, "psel");
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, acc_field_spfield_ctype, ctype, p_field, p_spfield, psel);
  return p_ret;
})

EXPORT(get_n_points_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  if (!PyArg_ParseTuple(args, "O", &p_field)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, get_n_points_spfield_ctype, ctype, pf);
  return p_ret;
})

EXPORT(get_multiplicity_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  if (!PyArg_ParseTuple(args, "O", &p_field)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, get_multiplicity_spfield_ctype, ctype, pf);
  return p_ret;
})

EXPORT(qnorm_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  if (!PyArg_ParseTuple(args, "O", &p_field)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, qnorm_spfield_ctype, ctype, pf);
  return p_ret;
})

EXPORT(qnorm_field_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  PyObject* p_field1 = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_field, &p_field1)) {
    return NULL;
  }
  SelectedPoints<double>& f = py_convert_type_spoints<double>(p_field);
  const std::string ctype = py_get_ctype(p_field1);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, qnorm_field_spfield_ctype, ctype, f, p_field1);
  return p_ret;
})

EXPORT(set_sqrt_double_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  PyObject* p_field1 = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_field, &p_field1)) {
    return NULL;
  }
  SelectedPoints<double>& f = py_convert_type_spoints<double>(p_field);
  const SelectedPoints<double>& f1 = py_convert_type_spoints<double>(p_field1);
  const int n_points = f1.n_points;
  const int multiplicity = f1.multiplicity;
  f.init();
  f.init(n_points, multiplicity);
  qacc_for(idx, f.n_points, {
    const Vector<double> f1v = f1.get_elems_const(idx);
    Vector<double> fv = f.get_elems(idx);
    for (int m = 0; m < multiplicity; ++m) {
      fv[m] = std::sqrt(f1v[m]);
    }
  });
  Py_RETURN_NONE;
})

EXPORT(get_elems_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  long idx = -1;
  if (!PyArg_ParseTuple(args, "Ol", &p_field, &idx)) {
    return NULL;
  }
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, get_elems_spfield_ctype, pf.ctype, pf, idx);
  return p_ret;
})

EXPORT(get_elem_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  long idx = -1;
  long m = -1;
  if (!PyArg_ParseTuple(args, "Ol|l", &p_field, &idx, &m)) {
    return NULL;
  }
  PyField pf = py_convert_field(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, get_elem_spfield_ctype, pf.ctype, pf, idx, m);
  return p_ret;
})

EXPORT(set_elems_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  long idx = -1;
  PyObject* p_val = NULL;
  if (!PyArg_ParseTuple(args, "OlO", &p_field, &idx, &p_val)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, set_elems_spfield_ctype, ctype, p_field, idx, p_val);
  return p_ret;
})

EXPORT(set_elem_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  long idx = -1;
  long m = -1;
  PyObject* p_val = NULL;
  if (!PyArg_ParseTuple(args, "OllO", &p_field, &idx, &m, &p_val)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, set_elem_spfield_ctype, ctype, p_field, idx, m, p_val);
  return p_ret;
})

EXPORT(save_complex_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  PyObject* p_path = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_field, &p_path)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  std::string path;
  py_convert(path, p_path);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, save_complex_spfield_ctype, ctype, pf, path);
  return p_ret;
})

EXPORT(load_complex_spfield, {
  using namespace qlat;
  PyObject* p_field = NULL;
  PyObject* p_path = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_field, &p_path)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  std::string path;
  py_convert(path, p_path);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, load_complex_spfield_ctype, ctype, pf, path);
  return p_ret;
})

EXPORT(lat_data_from_complex_spfield, {
  using namespace qlat;
  PyObject* p_ld = NULL;
  PyObject* p_field = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_ld, &p_field)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  LatData& ld = py_convert_type<LatData>(p_ld);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, lat_data_from_complex_spfield_ctype, ctype, ld, pf);
  return p_ret;
})

EXPORT(complex_spfield_from_lat_data, {
  using namespace qlat;
  PyObject* p_field = NULL;
  PyObject* p_ld = NULL;
  if (!PyArg_ParseTuple(args, "OO", &p_field, &p_ld)) {
    return NULL;
  }
  const std::string ctype = py_get_ctype(p_field);
  PyField pf = py_convert_field(p_field);
  const LatData& ld = py_convert_type<LatData>(p_ld);
  PyObject* p_ret = NULL;
  FIELD_DISPATCH(p_ret, complex_spfield_from_lat_data_ctype, ctype, pf, ld);
  return p_ret;
})
