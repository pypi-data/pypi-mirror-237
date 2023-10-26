#ifndef UTILS_QUDA_INVERTER_H
#define UTILS_QUDA_INVERTER_H

#pragma once

#include <qlat/qlat.h>

#include <quda.h>
////#include <gauge_force_quda.h>
#include <tune_quda.h>
#include <deflation.h>
#include <invert_quda.h>

#include <cstdlib>
#include "utils_float_type.h"
#include "quda_para.h"
#include "general_funs.h"
#include "utils_io_vec.h"
#include "utils_stagger_contractions.h"

static quda::TimeProfile profileEigensolve("eigensolveQuda");
static quda::TimeProfile profileInvertC("prefilesolveQudaC");

namespace qlat
{  //

//#define DIMCG        10
//#define DIMCG_DOUBLE 5

struct quda_inverter {
  long V;
  int X[4];
  QudaGaugeParam  gauge_param;
  ////void* quda_gf_default;
  qlat::vector<qlat::Complex > quda_gf_default;
  QudaInvertParam inv_param;
  quda::SolverParam solverParam;
  quda::Solver *solve_cg;
  bool CG_reset;

  Geometry geo;
  qlat::vector_acc<long > map_index;
  int solve_mode ;
  /////QudaInvertParam df_param;

  QudaEigParam    eig_param;
  int nvec;
  double inv_residue;
  double inv_time;
  int    inv_iter;
  double inv_gflops;
  int add_high;
  int num_src;
  int num_src_inv;

  ///std::vector<std::vector<quda::Complex > > evecs;

  quda::EigenSolver *eig_solveK;
  quda::EigenSolver *eig_solveF;
  quda::DiracMatrix* mat;
  quda::DiracMatrix* mat_E;
  quda::DiracMatrix* mat_pc;
  quda::DiracMatrix* mat_Mdag;
  quda::DiracMatrix* mat_MMdag;
  quda::DiracMatrix* mat_MdagM;

  quda::DiracM* m_cg;
  quda::DiracM* mSloppy;
  quda::DiracM* mPre;
  quda::DiracM* mEig;

  void* df_preconditioner;

  double mass_mat;
  //double mass_eig;
  double mass_value;

  ////eigen related
  quda::Dirac *dirac;
  quda::Dirac *dirac_pc;

  quda::Dirac *dirac_cg;
  quda::Dirac *dSloppy;
  quda::Dirac *dPre;
  quda::Dirac *dEig;

  std::vector<quda::Complex > evals_ZERO;
  std::vector<double        > evals_ERR ;

  std::vector<quda::ColorSpinorField > kSpace;
  std::vector<quda::ColorSpinorField > fSpace;
  ////std::vector<quda::ColorSpinorField > kSpace_cpu;
  std::vector<quda::Complex > evalsK;
  std::vector<quda::Complex > evalsF;

  std::vector<quda::ColorSpinorField > ZSpace;
  std::vector<quda::Complex > evalsZ;
  ///std::vector<quda::ColorSpinorField *> evecs_;
  int spinor_site_size;


  quda::ColorSpinorParam cs_cpu;
  quda::ColorSpinorParam cs_gpu;
  quda::ColorSpinorParam cs_gpuH;
  quda::ColorSpinorParam cs_gpuD;
  quda::ColorSpinorParam cs_gpuF;
  //quda::ColorSpinorParam cs_copy;

  //quda::ColorSpinorField *csrc, *cres;
  //quda::ColorSpinorField *cpu_src, *cpu_res;
  quda::ColorSpinorField *gsrc, *gres;
  quda::ColorSpinorField *gsrcH, *gresH;
  ///quda::ColorSpinorField *gsrcD, *gresD;
  quda::ColorSpinorField *gtmp1D, *gtmp2D;
  quda::ColorSpinorField *gtmp1F, *gtmp2F;
  quda::ColorSpinorField *gadd; ////for low mode addition

  quda::ColorSpinorField *ctmp0, *ctmp1, *ctmp2;
  quda::ColorSpinorField *gtmp0, *gtmp1, *gtmp2;
  //quda::ColorSpinorField *gsrcF, *gresF; ////format to match gpu solver
  ///bool singleE;

  ////0 for wilson, clover, 1 for stagger
  int fermion_type;
  bool gauge_with_phase;
  int use_eigen_pc;
  int check_residue;
  bool clover_alloc;

  std::vector<std::vector<quda::Complex > > quda_clover;
  std::vector<quda::Complex > quda_clover_inv;

  quda_inverter(const Geometry& geo_, QudaTboundary t_boundary, int num_src_=1);

  inline void free_mem();
  inline void setup_link(qlat::Complex* quda_gf, const int apply_stag_phase = 0);

  inline void setup_clover(const double clover_csw);
  inline void setup_stagger();

  inline void setup_eigen(const double mass, const int num_eigensys, const double err = 1e-12, const int eig_poly_deg=100, const double eig_amin = 0.1, const bool compute=true, const int nkr=-1, const double eig_amax = 0.0, const double qr_tol = 0.1, const int eig_check_interval = 10, const int eig_max_restarts = 100000, const int eig_batched_rotate = 0);
  inline void update_eigen_mass(const double mass, bool force = false);

  inline void setup_inc_eigencg(const int n_ev, const int n_kr, const int n_conv, const int df_grid, const double tol, const double inc_tol, const double tol_restart, const int restart_n, const int pipeline, const int inv_type = 1);

  template<typename Ty>
  inline void do_inv(Ty* res, Ty* src, const double mass, const double err = 1e-10, const int niter = 10000 , const int prec_type = 0);
  inline void deflate(quda::ColorSpinorField &sol, const quda::ColorSpinorField& src,
      std::vector<quda::ColorSpinorField> &evecs, const std::vector<quda::Complex> &evals, bool accumulate = false);

  inline void deflate(std::vector<quda::ColorSpinorField *> &sol, const std::vector<quda::ColorSpinorField *> &src,
      std::vector<quda::ColorSpinorField> &evecs, const std::vector<quda::Complex> &evals, bool accumulate = false);

  void print_plaq();

  inline void setup_inv_mass(const double mass);
  inline void clear_mat();
  inline void setup_mat_mass(const double mass, const bool force_do = false);
  inline void free_csfield(const int mode = 0);
  inline void alloc_csfield_cpu();
  inline void alloc_csfield_gpu();

  inline void save_evecs(const char* filename, const bool read = false, const int ndouble = -1, const int split_save = 1 );
  inline void save_evecsF(const char* filename, const bool read = false);
  inline void check_residualF();

  inline void setup_inv_param_prec(int prec_type = 0);
  inline void setup_gauge_param(QudaTboundary t_boundary);

  inline void random_src(const int seed);

  inline void reconstruct_full(const double mass = -1);
  inline void prepare_low_prop(int mode = 0);
  inline void save_prop(const void* srcP, const char* filename);

  inline void setup_CG();
  inline void clear_CG(){
    if(solve_cg != NULL){delete solve_cg;solve_cg = NULL;}
  }
  //inline void invertQuda_COPY(quda::ColorSpinorField& x, quda::ColorSpinorField& b, int solve_mode_ = 0);
  inline void invertQuda_COPY(quda::ColorSpinorField& res, quda::ColorSpinorField& src, int solve_mode_ = 0);

  ~quda_inverter();


};

inline void quda_inverter::setup_gauge_param(QudaTboundary t_boundary)
{
  TIMER("setup_gauge_param");
  for (int mu = 0; mu < 4; mu++) {gauge_param.X[mu] = X[mu];}

  ////tuning flag for not high mode

  gauge_param.type = QUDA_WILSON_LINKS; //// or QUDA_SU3_LINKS
  // Slowest changing to fastest changing: even-odd, mu, x_cb_4d, row, column,
  // complex See the code later in this file to see the conversion between
  // Grid inde and Quda index.
  gauge_param.gauge_order = QUDA_MILC_GAUGE_ORDER;

  gauge_param.t_boundary = t_boundary; ////fermion_t_boundary
  //gauge_param.t_boundary = QUDA_PERIODIC_T; ////fermion_t_boundary
  //QUDA_ANTI_PERIODIC_T

  ////fine tune the precisions if needed
  gauge_param.cpu_prec               = QUDA_DOUBLE_PRECISION;
  gauge_param.cuda_prec              = QUDA_DOUBLE_PRECISION;

  gauge_param.cuda_prec_sloppy       = QUDA_SINGLE_PRECISION;
  gauge_param.cuda_prec_precondition = QUDA_SINGLE_PRECISION;
  gauge_param.cuda_prec_eigensolver  = QUDA_SINGLE_PRECISION;

  //gauge_param.cuda_prec_sloppy       = QUDA_DOUBLE_PRECISION;
  //gauge_param.cuda_prec_precondition = QUDA_DOUBLE_PRECISION;
  //gauge_param.cuda_prec_eigensolver  = QUDA_DOUBLE_PRECISION;

  gauge_param.reconstruct                   = QUDA_RECONSTRUCT_NO;  ////gauge_param.reconstruct = link_recon;
  gauge_param.reconstruct_sloppy            = QUDA_RECONSTRUCT_NO;
  gauge_param.reconstruct_precondition      = QUDA_RECONSTRUCT_NO;
  gauge_param.reconstruct_eigensolver       = QUDA_RECONSTRUCT_NO;
  gauge_param.reconstruct_refinement_sloppy = QUDA_RECONSTRUCT_NO;  /////link_recon

  gauge_param.anisotropy = 1.0;

  // For HISQ, this must always be set to 1.0, since the tadpole
  // correction is baked into the coefficients for the first fattening.
  // The tadpole doesn't mean anything for the second fattening
  // since the input fields are unitarized.
  gauge_param.tadpole_coeff = 1.0;

  gauge_param.ga_pad = 0;
  gauge_param.mom_ga_pad = 0;

  /////gauge fix paras
  gauge_param.gauge_fix = QUDA_GAUGE_FIXED_NO;

  //////gauge_param.struct_size = sizeof(gauge_param);

  gauge_param.scale = 1.0;
  gauge_param.staggered_phase_type = QUDA_STAGGERED_PHASE_MILC;

  gauge_param.anisotropy = 1.0; /////anisotropy

  int pad_size = 0;
  // For multi-GPU, ga_pad must be large enough to store a time-slice
  int x_face_size = gauge_param.X[1] * gauge_param.X[2] * gauge_param.X[3] / 2;
  int y_face_size = gauge_param.X[0] * gauge_param.X[2] * gauge_param.X[3] / 2;
  int z_face_size = gauge_param.X[0] * gauge_param.X[1] * gauge_param.X[3] / 2;
  int t_face_size = gauge_param.X[0] * gauge_param.X[1] * gauge_param.X[2] / 2;
  pad_size = std::max({x_face_size, y_face_size, z_face_size, t_face_size});
  gauge_param.ga_pad = pad_size;
  gauge_param.struct_size = sizeof(gauge_param);
  ////===END of gauge_param
}

quda_inverter::quda_inverter(const Geometry& geo_, QudaTboundary t_boundary, int num_src_)
{
  TIMER("quda_inverter_constuctor");
  /////set up gauge parameters
  geo = geo_;
  V = geo.local_volume();
  qassert(num_src_ > 0);
  num_src = num_src_;
  num_src_inv = num_src;

  for (int mu = 0; mu < 4; mu++) {X[mu] = geo.node_site[mu];}
  ////===Start of gauge_param
  gauge_param = newQudaGaugeParam();
  ////quda_gf_default = NULL;
  inv_param   = newQudaInvertParam();

  setup_gauge_param(t_boundary);

  add_high = 1;
  solve_mode = 0;

  clover_alloc = false;
  //csrc = NULL; cres = NULL;
  gsrc = NULL; gres = NULL;
  gsrcH= NULL; gresH= NULL;
  //gsrcD= NULL; gresD= NULL;
  gtmp1D = NULL;gtmp2D = NULL;
  gtmp1F = NULL;gtmp2F = NULL;
  gadd = NULL;

  ctmp0 = NULL; ctmp1 = NULL; ctmp2 = NULL;
  gtmp0 = NULL; gtmp1 = NULL; gtmp2 = NULL;

  eig_solveK = NULL;
  eig_solveF = NULL;
  mat = NULL;
  mat_pc = NULL;
  mat_Mdag  = NULL;
  mat_MMdag = NULL;
  mat_E = NULL;
  mat_MdagM = NULL;

  m_cg = NULL;
  mSloppy = NULL;
  mPre = NULL;
  mEig = NULL;
  CG_reset = true;

  solve_cg = NULL;
  dirac = NULL;
  dirac_cg = NULL;
  dirac_pc = NULL;
  dSloppy = NULL;
  dPre    = NULL;
  dEig    = NULL;

  df_preconditioner = NULL;
  nvec = 0;
  use_eigen_pc = 0;
  check_residue = 0;

  spinor_site_size = 0;
  gauge_with_phase = false;

  mass_mat = -1000000;
  ///mass_eig = -1000000;
  mass_value  = -100000;
  inv_time = 0.0;
  inv_iter = 0;
  inv_gflops = 0.0;

}


inline void quda_inverter::setup_link(qlat::Complex* quda_gf, const int apply_stag_phase)
{
  TIMER("setup_link");
  /////load gauge to quda GPU default position
  if(apply_stag_phase == 1 and gauge_with_phase == false){
    applyGaugeFieldScaling_long((qlat::Complex*) quda_gf, V/2, &gauge_param, QUDA_STAGGERED_DSLASH);
    loadGaugeQuda((void *) quda_gf, &gauge_param);
    gauge_with_phase = true;
  }
  else{
    loadGaugeQuda((void *) quda_gf, &gauge_param);
    //print_plaq();
  }
  ////quda_gf_default = (void *) quda_gf; //required to reload gauge with prec
  if(quda_gf != quda_gf_default.data()){
    quda_gf_default.resize(V *3*3*4 );
    cpy_data_thread(&quda_gf_default[0], quda_gf, V*3*3*4, false);
  }
}

inline void quda_inverter::print_plaq()
{
  ///// Compute plaquette as a sanity check from interal GPU gauge
  double plaq[3];
  plaqQuda(plaq);
  QudaGaugeObservableParam param = newQudaGaugeObservableParam();
  param.compute_plaquette = QUDA_BOOLEAN_TRUE;
  param.compute_qcharge = QUDA_BOOLEAN_TRUE;
  gaugeObservablesQuda(&param);
  if(quda::comm_rank_global()== 0)printfQuda("Computed plaquette is %.8e (spatial = %.8e, temporal = %.8e), topological charge = %.8e \n",
      plaq[0], plaq[1], plaq[2],  param.qcharge);
}

////mode = 0 all field, mode = 1 cpu field , mode = 2 gpu field
inline void quda_inverter::free_csfield(const int mode)
{
  TIMER("free_csfield");
  if(mode == 0 or mode == 1){
  //if(csrc  != NULL){delete csrc;csrc=NULL;}if(cres != NULL){delete cres;cres=NULL;}
  if(ctmp0 != NULL){delete ctmp0;ctmp0=NULL;}
  if(ctmp1 != NULL){delete ctmp1;ctmp1=NULL;}
  if(ctmp2 != NULL){delete ctmp2;ctmp2=NULL;}
  }

  if(mode == 0 or mode == 2){
  //if(gsrcD != NULL){delete gsrcD;gsrcD=NULL;}if(gresD!= NULL){delete gresD;gresD=NULL;}
  if(gsrc  != NULL){delete gsrc ;gsrc =NULL;}if(gres != NULL){delete gres ;gres =NULL;}
  if(gsrcH != NULL){delete gsrcH;gsrcH=NULL;}if(gresH!= NULL){delete gresH;gresH=NULL;}
  if(gtmp0 != NULL){delete gtmp0;gtmp0=NULL;}

  if(gtmp1 != NULL){delete gtmp1;gtmp1=NULL;}
  if(gtmp2 != NULL){delete gtmp2;gtmp2=NULL;}
  if(gadd  != NULL){delete gadd;gadd=NULL;}
  }

  if(mode == 0 or mode == 3){
  if(gtmp1D!= NULL){delete gtmp1D;gtmp1D=NULL;}
  if(gtmp2D!= NULL){delete gtmp2D;gtmp2D=NULL;}
  if(gtmp1F!= NULL){delete gtmp1F;gtmp1F=NULL;}
  if(gtmp2F!= NULL){delete gtmp2F;gtmp2F=NULL;}}


}

inline void quda_inverter::alloc_csfield_gpu()
{
  TIMER("alloc_csfield_gpu");
  free_csfield(2);
  quda::ColorSpinorParam cs_tmp(cs_gpu);
  cs_tmp.setPrecision(inv_param.cuda_prec, inv_param.cuda_prec, true);
  gsrc  = quda::ColorSpinorField::Create(cs_tmp);
  gres  = quda::ColorSpinorField::Create(cs_tmp);
  gtmp0 = quda::ColorSpinorField::Create(cs_tmp);
  gtmp1 = quda::ColorSpinorField::Create(cs_tmp);
  gtmp2 = quda::ColorSpinorField::Create(cs_tmp);

  cs_gpuH.setPrecision(inv_param.cuda_prec, inv_param.cuda_prec, true);
  gsrcH = quda::ColorSpinorField::Create(cs_gpuH); 
  gresH = quda::ColorSpinorField::Create(cs_gpuH);
  //cs_tmp.setPrecision(QUDA_DOUBLE_PRECISION, QUDA_DOUBLE_PRECISION, true);
  //gsrcD = quda::ColorSpinorField::Create(cs_tmp);
  //gresD = quda::ColorSpinorField::Create(cs_tmp);
}

inline void quda_inverter::alloc_csfield_cpu()
{
  TIMER("alloc_csfield_cpu");
  free_csfield(1);
  //bool pc_solution = (inv_param.solution_type == QUDA_MATPC_SOLUTION) ||
  //  (inv_param.solution_type == QUDA_MATPCDAG_MATPC_SOLUTION);
  bool pc_solution = false;
  void* temV = NULL;
  quda::cpuGaugeField cpuGauge(gauge_param);
  quda::ColorSpinorParam cpuParam_tem(temV, inv_param, cpuGauge.X(), pc_solution, inv_param.input_location);
  cs_cpu = quda::ColorSpinorParam(cpuParam_tem);
  //cs_cpu.setPrecision(inv_param.cpu_prec);
  cs_cpu.setPrecision(QUDA_DOUBLE_PRECISION); ////double for all cpu cs field
  cs_cpu.create = QUDA_ZERO_FIELD_CREATE;
  cs_cpu.location = QUDA_CPU_FIELD_LOCATION;
  cs_cpu.is_composite  = true;
  cs_cpu.is_component  = false;
  cs_cpu.composite_dim = num_src;

  cs_gpu = quda::ColorSpinorParam(cs_cpu);cs_gpu.location = QUDA_CUDA_FIELD_LOCATION;
  cs_gpu.create = QUDA_ZERO_FIELD_CREATE;
  //cs_gpu.setPrecision(inv_param.cuda_prec, inv_param.cuda_prec, true);
  cs_gpu.setPrecision(QUDA_DOUBLE_PRECISION, QUDA_DOUBLE_PRECISION, true); ////double for all cpu cs field
  ////cs_gpu.setPrecision(inv_param.cuda_prec, inv_param.cuda_prec_eigensolver, true);

  cs_gpu.siteSubset = QUDA_FULL_SITE_SUBSET;
  //if (inv_param.solution_type == QUDA_MAT_SOLUTION || inv_param.solution_type == QUDA_MATDAG_MAT_SOLUTION) {
  //  cs_gpu.siteSubset = QUDA_FULL_SITE_SUBSET;
  //} else {
  //  cs_gpu.siteSubset = QUDA_PARITY_SITE_SUBSET;
  //  cs_gpu.x[0] /= 2;
  //}

  //cs_gpu.setPrecision(inv_param.cuda_prec, inv_param.cuda_prec_eigensolver, true);
  //cs_gpu.setPrecision(inv_param.cuda_prec, inv_param.cuda_prec, true);
  //cs_gpu.setPrecision(inv_param.cuda_prec_eigensolver, inv_param.cuda_prec_eigensolver, true);
  if(cs_gpu.nSpin != 1) cs_gpu.gammaBasis = QUDA_UKQCD_GAMMA_BASIS;

  //csrc  = quda::ColorSpinorField::Create(cs_cpu);
  //cres  = quda::ColorSpinorField::Create(cs_cpu);
  ctmp0 = quda::ColorSpinorField::Create(cs_cpu);
  ctmp1 = quda::ColorSpinorField::Create(cs_cpu);
  ctmp2 = quda::ColorSpinorField::Create(cs_cpu);

  //bool single_file=true;
  if(fermion_type == 0){pc_solution = false;}
  if(fermion_type == 1){pc_solution = true ;}
  quda::ColorSpinorParam gpuParam_tem(temV, inv_param, cpuGauge.X(), pc_solution, QUDA_CUDA_FIELD_LOCATION);

  cs_gpuH = gpuParam_tem;
  cs_gpuH.create = QUDA_ZERO_FIELD_CREATE;
  cs_gpuH.is_composite  = true;
  cs_gpuH.is_component  = false;
  cs_gpuH.composite_dim = num_src;


  cs_gpuF= quda::ColorSpinorParam(gpuParam_tem);
  cs_gpuF.create = QUDA_ZERO_FIELD_CREATE;
  cs_gpuF.setPrecision(QUDA_SINGLE_PRECISION, QUDA_SINGLE_PRECISION, true);
  cs_gpuF.is_composite  = false;
  cs_gpuF.is_component  = false;

  ////cs_gpuF.setPrecision(QUDA_DOUBLE_PRECISION, QUDA_DOUBLE_PRECISION, true);

  cs_gpuD= quda::ColorSpinorParam(gpuParam_tem);
  cs_gpuD.is_composite  = false;
  cs_gpuD.is_component  = false;
  cs_gpuD.create = QUDA_ZERO_FIELD_CREATE;
  cs_gpuD.setPrecision(QUDA_DOUBLE_PRECISION, QUDA_DOUBLE_PRECISION, true);

  //quda::ColorSpinorParam cs_gpu_tem = cs_gpu;
  //cs_gpu_tem.setPrecision(QUDA_SINGLE_PRECISION, QUDA_SINGLE_PRECISION, true);
  //gsrcF = quda::ColorSpinorField::Create(cs_gpu_tem);
  //////=====START construct Staggered color spin parameters
  //cs_cpu.nColor = 3;
  //cs_cpu.nSpin = 1;
  //cs_cpu.nDim = 5;
  //for (int d = 0; d < 4; d++) cs_cpu.x[d] = gauge_param.X[d];
  //bool pc = isPCSolution(inv_param.solution_type);
  //if (pc) cs_cpu.x[0] /= 2;
  //cs_cpu.x[4] = 1;
  //cs_cpu.pc_type = QUDA_4D_PC;
  //cs_cpu.siteSubset = pc ? QUDA_PARITY_SITE_SUBSET : QUDA_FULL_SITE_SUBSET;
  //// Lattice vector data properties
  //cs_cpu.setPrecision(inv_param.cpu_prec);
  //cs_cpu.pad = 0;
  //cs_cpu.siteOrder = QUDA_EVEN_ODD_SITE_ORDER;
  //cs_cpu.fieldOrder = QUDA_SPACE_SPIN_COLOR_FIELD_ORDER;
  //cs_cpu.gammaBasis = inv_param.gamma_basis;
  //cs_cpu.create = QUDA_ZERO_FIELD_CREATE;
  //cs_cpu.location = QUDA_CPU_FIELD_LOCATION;
  //////=====END construct Staggered color spin parameters


}

/////double prec prop save
inline void quda_inverter::save_prop(const void* srcP, const char* filename)
{
  TIMER("quda save_prop");
  ////qlat::Coordinate total_site;
  ////qlat::Coordinate node_site = qlat::get_size_node();
  ////for(int d=0;d<4;d++){total_site[d] = X[d] * node_site[d];}
  ////qlat::Geometry geo;geo.init(total_site, 1);

  const int n0 = 1;
  std::vector<qlat::FieldM<qlat::Complex , 3> > prop;prop.resize(n0);
  for(int n = 0; n < prop.size(); n++){prop[n].init(geo);}

  qlat::Complex* src = (qlat::Complex*) srcP;
  long Nvol = geo.local_volume() * n0 ;

  for(int n=0;n<n0;n++){
    quda_cf_to_qlat_cf(prop[n], &src[n*Nvol]);
  }   

  std::string VECS_TYPE("STAGGERED_Prop");
  char infoL[500];sprintf(infoL,"mass %.8f", inv_param.mass);
  std::string INFO_LIST(infoL);

  bool single_file = false;
  bool read = false;
  qlat::load_qlat_noisesT(filename, prop, read, single_file, VECS_TYPE, std::string("NONE"), 0, n0, false);
}

inline void quda_inverter::save_evecsF(const char* filename, const bool read)
{
  TIMERB("save_evecsF");
  if(nvec <= 0 ){return ;}
  char filename0[600];char filename1[600];
  sprintf(filename0, "%s.full", filename);
  double mre = 0.0;

  //for (int i = 0; i < kSpace.size(); i++){delete kSpace[i];}kSpace.resize(0);
  //for (int i = 0; i < fSpace.size(); i++){delete fSpace[i];}fSpace.resize(0);
  kSpace.resize(0);fSpace.resize(0);

  quda::ColorSpinorField& c0 = (*ctmp0).Component(0);
  ////quda::ColorSpinorField& c1 = (*ctmp1).Component(0);

  int n0 = 0;
  if(read == true)
  {
    inputpara in0;////inputpara in1;
    in0.load_para(filename0, false);
    n0 = in0.nvec;

    ///read eigen value masses
    std::vector<std::string > mL0 = stringtolist(in0.INFO_LIST);
    double mi0 = stringtodouble(mL0[1]);
    mre= mi0;
  }else{n0 = ZSpace.size();}

  std::vector<qlat::FieldM<qlat::Complex , 3> > eigD;eigD.resize(n0);

  qlat::Coordinate total_site;
  qlat::Coordinate node_site = qlat::get_size_node();
  for(int d=0;d<4;d++){total_site[d] = X[d] * node_site[d];}
  qlat::Geometry geo;geo.init(total_site, 1);

  for(int n = 0; n < eigD.size(); n++){eigD[n].init(geo);}

  if(read == true)
  {
    //for (int i = 0; i < ZSpace.size(); i++){delete ZSpace[i];}ZSpace.resize(0);
    //for(int n=0;n<n0;n++)ZSpace.push_back(quda::ColorSpinorField::Create(cs_gpu));
    ZSpace.resize(n0);
    for(int n=0;n<n0;n++)ZSpace[n] = quda::ColorSpinorField(cs_gpu);
  }

  if(read == false)
  for(int n=0;n<n0;n++){
    (c0) = (ZSpace[n]);
    quda_cf_to_qlat_cf(eigD[n], (qlat::Complex*) c0.V());
  }   


  std::string VECS_TYPE("STAGGERED_Eigensystem");
  char infoL[500];sprintf(infoL,"mass %.8f", mass_value);
  std::string INFO_LIST(infoL);

  bool single_file = false;
  qlat::load_qlat_noisesT(filename0, eigD, read, single_file, VECS_TYPE, INFO_LIST, 0, n0, false);

  if(read == true )
  for(int n=0;n<n0;n++){
    qlat_cf_to_quda_cf((qlat::Complex*) c0.V(),  eigD[n]);
    (ZSpace[n]) = (c0);
  }   

  sprintf(filename1, "%s.evals", filename0);
  std::vector<double > values, errors;
  values.resize(2*n0); errors.resize(n0);
  if(read == false){
    qassert(evalsZ.size() != evals_ZERO.size());
    qassert(evals_ZERO.size() != 0 and evals_ERR.size() != 0);
    for(int n=0;n<nvec;n++){
      values[n*2+0] = evals_ZERO[n].real();
      values[n*2+1] = evals_ZERO[n].imag();
      errors[n] = evals_ERR[n]; 
    }
    save_gwu_eigenvalues(values, errors, filename1, "Staggered Fermions");
  }

  if(read == true){
    load_gwu_eigenvalues(values, errors, filename1);qassert(n0 <= values.size());
    evals_ZERO.resize(n0);evals_ERR.resize(n0);
    /////for(int n=  0;n<n0;n++){evals_ZERO[n] = quda::Complex(values[n*2+0], values[n*2+1]);}    
    for(int n=  0;n<n0;n++){evals_ZERO[n] = quda::Complex(values[n*2+0] - 4.0*mre*mre, values[n*2+1]);}    
    for(int n=  0;n<n0;n++){evals_ERR[ n] = errors[n];}    

    evalsZ.resize(n0);evalsK.resize(n0, 0.0);evalsF.resize(0, 0.0);
    update_eigen_mass(0.0, true);
  }
}

inline void quda_inverter::save_evecs(const char* filename, const bool read, const int ndouble, const int split_save )
{
  TIMERB("save_evecs");
  if(nvec <= 0){return ;}
  ////qassert(nvec == kSpace.size());qassert(nvec == evals.size());
  //bool singleE = false;
  //if(compute == true ){singleE = false;}
  //if(compute == false){singleE = true;}

  char filename0[600];char filename1[600];
  sprintf(filename0, "%s", filename);
  sprintf(filename1, "%s.single", filename);
  double mre = 0.0;
  quda::ColorSpinorField& c0 = (*ctmp0).Component(0);

  int nsave = nvec;
  if(fermion_type == 1){
    nsave = nvec/2;
    if(nvec%2 != 0){print0("Even Odd savings, nvec%2 != 0, nvec %d \n");qassert(false);}
  }

  //bool single_file=true;
  bool single_file=false;
  std::string VECS_TYPE("STAGGERED_Eigensystem");
  char infoL[500];
  sprintf(infoL,"mass %.8f", mass_value);
  std::string INFO_LIST(infoL);

  int n0 = nsave;int n1 = 0;
  if(read == false){
    if(split_save == 0){n0=nsave;n1=0;}
    if(split_save == 1){
    if(ndouble < 0 or ndouble >= nvec){
      n0 = nsave;n1=0;}
    else{
      n0 = ndouble;if(fermion_type == 1){n0 = ndouble/2;}
      n1 = nsave - n0;}
    }
  }else{
    ////ndouble no meaning here
    //inputpara in0;inputpara in1;
    //in0.load_para(filename0, false);
    //n0 = in0.nvec;
    //if(nsave <= n0){n0 = nsave;n1 = 0;}
    //else{
    //  in1.load_para(filename1, false);n1 = in1.nvec;
    //  qassert(nsave <= n0+n1);
    //  n1 = nsave - n0  ;
    //}

    inputpara in0;inputpara in1;
    if(split_save == 0){
      in0.load_para(filename0, false);
      n0 = in0.nvec;
      qassert(n0 >= nsave);
      if(ndouble == -1 or ndouble >= nvec){
        n0 = nsave;n1=0;
      }
      else{
        n0 = ndouble;if(fermion_type == 1){n0 = ndouble/2;}
        n1 = nsave - n0;
      }

      ///read eigen value masses
      std::vector<std::string > mL0 = stringtolist(in0.INFO_LIST);
      double mi0 = stringtodouble(mL0[1]);
      mre = mi0;
    }

    if(split_save == 1){
      ////ignore ndouble
      in0.load_para(filename0, false);
      in1.load_para(filename1, false);
      qassert(in0.nvec + in1.nvec >= nsave);
      if(nsave <= in0.nvec){n0 = nsave;n1 = 0;}
      if(nsave  > in0.nvec){n0 = in0.nvec;n1 = nsave -n0 ;}

      ///read eigen value masses
      std::vector<std::string > mL0 = stringtolist(in0.INFO_LIST);
      std::vector<std::string > mL1 = stringtolist(in1.INFO_LIST);
      double mi0 = stringtodouble(mL0[1]);
      double mi1 = stringtodouble(mL1[1]);
      qassert(mi0 == mi1);
      mre = mi0;
    }

  }

  int ns0 = n0;int ns1 = n1;
  if(nsave == nvec/2){ns0 = n0*2;ns1 = n1*2;}

  qlat::Coordinate total_site;
  qlat::Coordinate node_site = qlat::get_size_node();
  for(int d=0;d<4;d++){total_site[d] = X[d] * node_site[d];}
  qlat::Geometry geo;geo.init(total_site, 1);

  //std::vector<qlat::FieldM<qlat::ComplexF, 3> > eig;eig.resize(nsave);
  long Nvol = geo.local_volume() * spinor_site_size;
  std::vector<qlat::FieldM<qlat::Complex , 3> > eigD;eigD.resize(n0);
  //////if(read == false){eigD.resize(n0 + n1);}
  for(int n = 0; n < eigD.size(); n++){eigD[n].init(geo);}

  std::vector<qlat::FieldM<qlat::ComplexF, 3> > eigF;eigF.resize(n1);
  for (int n = 0; n < eigF.size(); n++){eigF[n].init(geo);}


  if(read == false){
    for(int n = 0; n < n0; n++){
      if(fermion_type == 0){c0 = (kSpace[n]);}
      if(fermion_type == 1){
        c0.Even() = (kSpace[2*n+0]);
        c0.Odd()  = (kSpace[2*n+1]);
      }
      //qlat::Complex* q = (qlat::Complex*) qlat::get_data(buf).data();
      //cpy_data_thread(q, (qlat::Complex*) ctmp0->V(), Nvol, 0);
      quda_cf_to_qlat_cf(eigD[n], (qlat::Complex*) c0.V());
    }

    ////Maybe needed
    //eig_solveK->orthonormalizeMGS(fSpace, ns1);
    for(int n = 0; n < n1; n++){
      if(fermion_type == 0){c0 = (kSpace[n + n0]);}
      if(fermion_type == 1){
        c0.Even() = (kSpace[2*(n+n0)+0]);
        c0.Odd()  = (kSpace[2*(n+n0)+1]);
      }
      //qlat::Complex* q = (qlat::Complex*) qlat::get_data(buf).data();
      //cpy_data_thread(q, (qlat::Complex*) ctmp0->V(), Nvol, 0);
      quda_cf_to_qlat_cf(eigF[n], (qlat::Complex*) c0.V());
    }
  }

  if(read == false){
    if(n0!=0){single_file = false;qlat::load_qlat_noisesT(filename0, eigD, read, single_file, VECS_TYPE, INFO_LIST, 0, n0, false);}
    if(n1!=0){single_file = true ;qlat::load_qlat_noisesT(filename1, eigF, read, single_file, VECS_TYPE, INFO_LIST, 0, n1, false);}

  }
  if(read == true){
    if(n0!=0){qlat::load_qlat_noisesT(filename0, eigD, read, single_file, VECS_TYPE, INFO_LIST, 0,   n0, false);}

    if(split_save == 0)
    if(n1!=0){qlat::load_qlat_noisesT(filename0, eigF, read, single_file, VECS_TYPE, INFO_LIST,n0,n0+n1, false);}
    if(split_save == 1)
    if(n1!=0){qlat::load_qlat_noisesT(filename1, eigF, read, single_file, VECS_TYPE, INFO_LIST, 0,   n1, false);}
  }

  /////===load to gpu
  if(read == true){
  //for (int i = 0; i < kSpace.size(); i++) delete kSpace[i];kSpace.resize(0);
  //for (int i = 0; i < fSpace.size(); i++) delete fSpace[i];fSpace.resize(0);
  kSpace.resize(ns0);
  fSpace.resize(ns1);

  eig_param.n_ev_deflate = ns0;eig_solveK = quda::EigenSolver::create(&eig_param, *mat_E, profileEigensolve);
  eig_param.n_ev_deflate = ns1;eig_solveF = quda::EigenSolver::create(&eig_param, *mat_E, profileEigensolve);
  quda::ColorSpinorParam csD = quda::ColorSpinorParam(cs_gpuD);
  quda::ColorSpinorParam csF = quda::ColorSpinorParam(cs_gpuF);
  csD.is_composite  = false;csD.is_component  = false;
  csF.is_composite  = false;csF.is_component  = false;


  for(int n = 0; n < ns0; n++){kSpace[n] = quda::ColorSpinorField(csD);}
  for(int n = 0; n < ns1; n++){fSpace[n] = quda::ColorSpinorField(csF);}
  for(int n = 0; n < n0; n++){
    qlat_cf_to_quda_cf((qlat::Complex*) c0.V(), eigD[n]);
    if(fermion_type == 0){(kSpace[n]) = c0;}
    if(fermion_type == 1){
      (kSpace[2*n+0]) = c0.Even();
      (kSpace[2*n+1]) = c0.Odd() ;
    }
  }

  for(int n = 0; n < n1; n++){
    qlat_cf_to_quda_cf((qlat::Complex*) c0.V(), eigF[n]);
    if(fermion_type == 0){(fSpace[n]) = c0;}
    if(fermion_type == 1){
      (fSpace[2*n+0]) = c0.Even();
      (fSpace[2*n+1]) = c0.Odd() ;
    }
  }
  }
  //eig_solveF->orthonormalizeMGS(fSpace, ns1);

  char fileE[600];
  sprintf(fileE,"%s.evals", filename);

  std::vector<double > values, errors;
  values.resize(2*nvec); errors.resize(nvec);
  if(read == false){
    qassert(evals_ZERO.size() != 0 and evals_ERR.size() != 0);
    for(int n=0;n<nvec;n++){
      values[n*2+0] = evals_ZERO[n].real();
      values[n*2+1] = evals_ZERO[n].imag();
      errors[n] = evals_ERR[n]; 
    }
    save_gwu_eigenvalues(values, errors, fileE, "Staggered Fermions");
  }

  if(read == true){
    load_gwu_eigenvalues(values, errors, fileE);qassert(ns0 + ns1 <= values.size()/2);

    evals_ZERO.resize(ns0+ns1);evals_ERR.resize(ns0+ns1);
    for(int n=  0;n<ns0+ns1;n++){evals_ZERO[n] = quda::Complex(values[n*2+0] - 4.0*mre*mre, values[n*2+1]);}    

    for(int n=  0;n<ns0+ns1;n++){evals_ERR[ n] = errors[n];}    

    evalsK.resize(ns0, 0.0);evalsF.resize(ns1, 0.0);
    update_eigen_mass(0.0, true);
  }

}

inline void quda_inverter::free_mem(){
  TIMER("quda free_mem");
  V = 0;
  for(int i=0;i<4;i++){X[i] = 0;}

  //for (int i = 0; i < evecs_.size(); i++) delete evecs_[i];
  //evecs_.resize(0);
  //evecs.resize(0);
  kSpace.resize(0);
  fSpace.resize(0);
  ZSpace.resize(0);
  ////kSpace_cpu.resize(0);
  //for (int i = 0; i < kSpace.size(); i++) delete kSpace[i];kSpace.resize(0);
  //for (int i = 0; i < fSpace.size(); i++) delete fSpace[i];fSpace.resize(0);
  //for (int i = 0; i < ZSpace.size(); i++) delete ZSpace[i];ZSpace.resize(0);
  //for (int i = 0; i < kSpace_cpu.size(); i++) delete kSpace_cpu[i];kSpace_cpu.resize(0);
  evalsK.resize(0);
  evalsF.resize(0);
  evalsZ.resize(0);
  free_csfield();

  if(eig_solveF != NULL){delete eig_solveF;eig_solveF=NULL;}
  if(eig_solveK != NULL){delete eig_solveK;eig_solveK=NULL;}
  nvec = 0;

  if(df_preconditioner != NULL){destroyDeflationQuda(df_preconditioner);df_preconditioner=NULL;}
  clear_CG();
  clear_mat();
}

inline void quda_inverter::setup_clover(const double clover_csw)
{
  fermion_type = 0;
  if(fermion_type == 0){spinor_site_size = 12;}

  /////===Start of Inv parameters
  inv_param.dslash_type = QUDA_CLOVER_WILSON_DSLASH;

  /////double kappa      = kappa;
  double anisotropy = gauge_param.anisotropy;
  inv_param.kappa = 0.150;
  inv_param.mass = 0.5 / inv_param.kappa - (1.0 + 3.0 / anisotropy);

  // Use 3D or 4D laplace
  //===inv_param.laplace3D = laplace3D;
  inv_param.Ls = 1;

  inv_param.cpu_prec                      = QUDA_DOUBLE_PRECISION;
  inv_param.cuda_prec                     = QUDA_DOUBLE_PRECISION;
  inv_param.cuda_prec_sloppy              = QUDA_SINGLE_PRECISION;
  inv_param.cuda_prec_refinement_sloppy   = QUDA_SINGLE_PRECISION;


  inv_param.preserve_source = QUDA_PRESERVE_SOURCE_YES;
  inv_param.gamma_basis = QUDA_DEGRAND_ROSSI_GAMMA_BASIS;
  inv_param.dirac_order = QUDA_DIRAC_ORDER;


  inv_param.clover_cpu_prec               = QUDA_DOUBLE_PRECISION;
  inv_param.clover_cuda_prec              = QUDA_DOUBLE_PRECISION;

  inv_param.clover_cuda_prec_sloppy       = QUDA_SINGLE_PRECISION;
  inv_param.clover_cuda_prec_refinement_sloppy = QUDA_SINGLE_PRECISION;

  ////related to eigensystem
  inv_param.cuda_prec_eigensolver         = QUDA_SINGLE_PRECISION;
  inv_param.cuda_prec_precondition        = QUDA_SINGLE_PRECISION;
  inv_param.clover_cuda_prec_precondition = QUDA_SINGLE_PRECISION;
  inv_param.clover_cuda_prec_eigensolver  = QUDA_SINGLE_PRECISION;

  inv_param.clover_order = QUDA_PACKED_CLOVER_ORDER;
  // Use kappa * csw or supplied clover_coeff
  bool compute_clover_trlog = false;
  //bool compute_clover_trlog = true;
  inv_param.clover_csw = clover_csw;
  inv_param.clover_coeff = inv_param.clover_csw * inv_param.kappa;
  /////===unknow para
  inv_param.compute_clover_trlog = compute_clover_trlog ? 1 : 0;

  // General parameter setup
  inv_param.inv_type = QUDA_CG_INVERTER;

  // solution_type specifies *what* system is to be solved.
  // solve_type specifies *how* the system is to be solved.
  //
  // We have the following four cases (plus preconditioned variants):
  //
  // solution_type    solve_type    Effect
  // -------------    ----------    ------
  // MAT              DIRECT        Solve Ax=b
  // MATDAG_MAT       DIRECT        Solve A^dag y = b, followed by Ax=y
  // MAT              NORMOP        Solve (A^dag A) x = (A^dag b)
  // MATDAG_MAT       NORMOP        Solve (A^dag A) x = b
  // MAT              NORMERR       Solve (A A^dag) y = b, then x = A^dag y
  //
  // We generally require that the solution_type and solve_type
  // preconditioning match.  As an exception, the unpreconditioned MAT
  // solution_type may be used with any solve_type, including
  // DIRECT_PC and NORMOP_PC.  In these cases, preparation of the
  // preconditioned source and reconstruction of the full solution are
  // taken care of by Dirac::prepare() and Dirac::reconstruct(),
  // respectively.

  // Eventually we want the unpreconditioned solution.
  inv_param.solution_type = QUDA_MAT_SOLUTION;

  // NORMOP_PC means preconditioned normal operator MdagM
  //inv_param.solve_type = QUDA_NORMOP_PC_SOLVE;
  inv_param.solve_type = QUDA_NORMOP_SOLVE;

  // There might be a performance difference.
  inv_param.matpc_type = QUDA_MATPC_EVEN_EVEN;

  inv_param.dagger = QUDA_DAG_NO;

  //inv_param.mass_normalization   = QUDA_KAPPA_NORMALIZATION;
  inv_param.mass_normalization   = QUDA_MASS_NORMALIZATION;
  inv_param.solver_normalization =  QUDA_SOURCE_NORMALIZATION;
  //inv_param.solver_normalization = QUDA_DEFAULT_NORMALIZATION;
  //inv_param.solver_normalization = QUDA_KAPPA_NORMALIZATION;

  ///unknown
  int gcrNkrylov = 10;
  QudaCABasis ca_basis = QUDA_POWER_BASIS;
  double ca_lambda_min = 0.0;
  double ca_lambda_max = -1.0;

  inv_param.pipeline = 1;
  inv_param.Nsteps = 2;
  inv_param.gcrNkrylov = gcrNkrylov;
  inv_param.ca_basis = ca_basis;
  inv_param.ca_lambda_min = ca_lambda_min;
  inv_param.ca_lambda_max = ca_lambda_max;

  inv_param.tol     = 1e-10;
  inv_param.maxiter = 100000;
  inv_param.tol_restart = 0.0005;
  //if (tol_hq == 0 && tol == 0) {
  //  errorQuda("qudaInvert: requesting zero residual\n");
  //  exit(1);
  //}

  // require both L2 relative and heavy quark residual to determine convergence
  inv_param.residual_type = static_cast<QudaResidualType_s>(0);
  inv_param.residual_type = static_cast<QudaResidualType_s>(inv_param.residual_type | QUDA_L2_RELATIVE_RESIDUAL);

  inv_param.tol_hq = 1e-5; // specify a tolerance for the residual for heavy quark residual
  //inv_param.tol_hq = 1e-10; // specify a tolerance for the residual for heavy quark residual

  //// Offsets used only by multi-shift solver
  //// These should be set in the application code. We set the them here by way of
  //// example
  //inv_param.num_offset = multishift;
  //for (int i = 0; i < inv_param.num_offset; i++) inv_param.offset[i] = 0.06 + i * i * 0.1;
  //// these can be set individually
  //for (int i = 0; i < inv_param.num_offset; i++) {
  //  inv_param.tol_offset[i] = inv_param.tol;
  //  inv_param.tol_hq_offset[i] = inv_param.tol_hq;
  //}

  // This is for Quda's sophisticated reliable update. 0.1 should be good.
  inv_param.reliable_delta = 0.1;
  inv_param.use_alternative_reliable = true;
  inv_param.use_sloppy_partial_accumulator = 0;
  inv_param.solution_accumulator_pipeline = 1;
  inv_param.max_res_increase = 1;

  // domain decomposition preconditioner parameters
  // inv_param.inv_type_precondition = precon_type;

  //inv_param.schwarz_type = precon_schwarz_type;
  //inv_param.precondition_cycle = precon_schwarz_cycle;
  //inv_param.tol_precondition = tol_precondition;
  //inv_param.maxiter_precondition = maxiter_precondition;
  //inv_param.omega = 1.0;

  inv_param.input_location  = QUDA_CPU_FIELD_LOCATION;
  inv_param.output_location = QUDA_CPU_FIELD_LOCATION;

  // QUDA_DEBUG_VERBOSE is too nasty.

  inv_param.extlib_type = QUDA_EIGEN_EXTLIB;

  // Whether or not to use native BLAS LAPACK
  //inv_param.native_blas_lapack = (native_blas_lapack ? QUDA_BOOLEAN_TRUE : QUDA_BOOLEAN_FALSE);
  inv_param.native_blas_lapack = QUDA_BOOLEAN_TRUE;

  //// Whether or not use fused kernels for Mobius
  ////inv_param.use_mobius_fused_kernel = use_mobius_fused_kernel ? QUDA_BOOLEAN_TRUE : QUDA_BOOLEAN_FALSE;
  //inv_param.use_mobius_fused_kernel = QUDA_BOOLEAN_FALSE;


  ///////===check this variable
  std::array<int, 4> grid_partition = {1, 1, 1, 1};
  inv_param.split_grid[0] = grid_partition[0];
  inv_param.split_grid[1] = grid_partition[1];
  inv_param.split_grid[2] = grid_partition[2];
  inv_param.split_grid[3] = grid_partition[3];

  inv_param.struct_size = sizeof(inv_param);

  ////===END of Inv parameters

  ///int do_inv = 1;
  {
  //////===operator define
  //void *clover = nullptr;
  //void *clover_inv = nullptr;

  int clover_site_size           = 72; // real numbers per block-diagonal clover matrix
  ////size_t host_clover_data_type_size = (cpu_prec == QUDA_DOUBLE_PRECISION) ? sizeof(double) : sizeof(float);
  int host_clover_data_type_size = sizeof(quda::Complex)/2;
  ////size_t host_spinor_data_type_size = (cpu_prec == QUDA_DOUBLE_PRECISION) ? sizeof(double) : sizeof(float);
  int host_spinor_data_type_size = sizeof(quda::Complex)/2;

  quda_clover.resize(    V * clover_site_size * host_clover_data_type_size);
  quda_clover_inv.resize(V * clover_site_size * host_spinor_data_type_size);

  //constructHostCloverField((void*) quda_clover.data(), (void*) quda_clover_inv.data(), inv_param);
  /////===host

  bool compute_clover = true;
  //if(in.clover_csw == 0){compute_clover = false;}
  //double norm = 0.00; // clover components are random numbers in the range (-norm, norm)
  //double diag = 1.0;  // constant added to the diagonal
  ////if (!compute_clover) constructQudaCloverField((void*) quda_clover.data(), norm, diag, inv_param.clover_cpu_prec, V);
  inv_param.compute_clover = compute_clover;
  if (compute_clover) inv_param.return_clover = 1;
  inv_param.compute_clover_inverse = 1;
  inv_param.return_clover_inverse  = 1;

  //loadCloverQuda((void*) quda_clover.data(), (void*)  quda_clover_inv.data(), &inv_param);
  //if(in.clover_csw == 0){
  //inv_param.compute_clover_inverse = 0;
  //inv_param.return_clover_inverse  = 0;
  //}
  /////===host
  ///// Load the clover terms to the device
  //loadCloverQuda((void*) quda_clover.data(), (void*)  quda_clover_inv.data(), &inv_param);
  //loadCloverQuda((void*) quda_clover.data(), (void*)  quda_clover_inv.data(), &inv_param);
  loadCloverQuda((void*) quda_clover.data(), (void*)  quda_clover_inv.data(), &inv_param);
  }

  alloc_csfield_cpu();
  alloc_csfield_gpu();

}

inline void quda_inverter::setup_stagger()
{
  TIMER("setup_stagger");
  fermion_type = 1;
  if(fermion_type == 1){spinor_site_size = 3 ;}
  if(gauge_with_phase == false){errorQuda("Quda stagger need link phases! \n");}

  /////===Start of Inv parameters
  inv_param.dslash_type = QUDA_STAGGERED_DSLASH;
  ////inv_param.mass  = fermion_mass;
  //inv_param.mass  = 0.2;
  inv_param.mass  = 0.2;

  // Use 3D or 4D laplace
  //===inv_param.laplace3D = laplace3D;
  inv_param.Ls = 1;

  inv_param.cpu_prec                      = QUDA_DOUBLE_PRECISION;
  inv_param.cuda_prec                     = QUDA_DOUBLE_PRECISION;
  //inv_param.cuda_prec_precondition   = QUDA_DOUBLE_PRECISION;

  inv_param.cuda_prec_sloppy              = QUDA_SINGLE_PRECISION;
  inv_param.cuda_prec_refinement_sloppy   = QUDA_SINGLE_PRECISION;
  inv_param.preserve_source = QUDA_PRESERVE_SOURCE_YES;
  inv_param.gamma_basis = QUDA_DEGRAND_ROSSI_GAMMA_BASIS;
  inv_param.dirac_order = QUDA_DIRAC_ORDER;

  ////related to eigensystem
  inv_param.cuda_prec_eigensolver         = QUDA_SINGLE_PRECISION;
  inv_param.cuda_prec_precondition        = QUDA_SINGLE_PRECISION;

  // General parameter setup
  inv_param.inv_type = QUDA_CG_INVERTER;

  // solution_type specifies *what* system is to be solved.
  // solve_type specifies *how* the system is to be solved.
  //
  // We have the following four cases (plus preconditioned variants):
  //
  // solution_type    solve_type    Effect
  // -------------    ----------    ------
  // MAT              DIRECT        Solve Ax=b
  // MATDAG_MAT       DIRECT        Solve A^dag y = b, followed by Ax=y
  // MAT              NORMOP        Solve (A^dag A) x = (A^dag b)
  // MATDAG_MAT       NORMOP        Solve (A^dag A) x = b
  // MAT              NORMERR       Solve (A A^dag) y = b, then x = A^dag y
  //
  // We generally require that the solution_type and solve_type
  // preconditioning match.  As an exception, the unpreconditioned MAT
  // solution_type may be used with any solve_type, including
  // DIRECT_PC and NORMOP_PC.  In these cases, preparation of the
  // preconditioned source and reconstruction of the full solution are
  // taken care of by Dirac::prepare() and Dirac::reconstruct(),
  // respectively.

  // Eventually we want the unpreconditioned solution.
  inv_param.solution_type = QUDA_MAT_SOLUTION;

  // NORMOP_PC means preconditioned normal operator MdagM
  //inv_param.solve_type = QUDA_NORMOP_PC_SOLVE;
  ////inv_param.solve_type = QUDA_DIRECT_PC_SOLVE;
  inv_param.solve_type = QUDA_DIRECT_PC_SOLVE;
  //inv_param.solve_type = QUDA_NORMOP_SOLVE;
  //if(in.solver_type == 0){inv_param.solve_type = QUDA_DIRECT_PC_SOLVE;}
  //if(in.solver_type == 1){inv_param.solve_type = QUDA_NORMERR_PC_SOLVE;}
  //if(in.solver_type == 2){inv_param.solve_type = QUDA_NORMOP_PC_SOLVE;}


  // There might be a performance difference.
  inv_param.matpc_type = QUDA_MATPC_EVEN_EVEN;

  inv_param.dagger = QUDA_DAG_NO;

  //inv_param.mass_normalization   = QUDA_KAPPA_NORMALIZATION;
  inv_param.mass_normalization   = QUDA_MASS_NORMALIZATION;
  inv_param.solver_normalization =  QUDA_SOURCE_NORMALIZATION;
  //inv_param.solver_normalization = QUDA_DEFAULT_NORMALIZATION;
  //inv_param.solver_normalization = QUDA_KAPPA_NORMALIZATION;

  ///unknown
  int gcrNkrylov = 10;
  QudaCABasis ca_basis = QUDA_POWER_BASIS;
  double ca_lambda_min = 0.0;
  double ca_lambda_max = -1.0;

  inv_param.pipeline = 1;
  inv_param.Nsteps = 2;
  inv_param.gcrNkrylov = gcrNkrylov;
  inv_param.ca_basis = ca_basis;
  inv_param.ca_lambda_min = ca_lambda_min;
  inv_param.ca_lambda_max = ca_lambda_max;

  inv_param.tol     = 1e-10;
  inv_param.maxiter = 100000;
  inv_param.tol_restart = 0.0005;
  //if (tol_hq == 0 && tol == 0) {
  //  errorQuda("qudaInvert: requesting zero residual\n");
  //  exit(1);
  //}

  // require both L2 relative and heavy quark residual to determine convergence
  inv_param.residual_type = static_cast<QudaResidualType_s>(0);
  inv_param.residual_type = static_cast<QudaResidualType_s>(inv_param.residual_type | QUDA_L2_RELATIVE_RESIDUAL);

  inv_param.tol_hq = 1e-5; // specify a tolerance for the residual for heavy quark residual
  //inv_param.tol_hq = 1e-10; // specify a tolerance for the residual for heavy quark residual

  //// Offsets used only by multi-shift solver
  //// These should be set in the application code. We set the them here by way of
  //// example
  //inv_param.num_offset = multishift;
  //for (int i = 0; i < inv_param.num_offset; i++) inv_param.offset[i] = 0.06 + i * i * 0.1;
  //// these can be set individually
  //for (int i = 0; i < inv_param.num_offset; i++) {
  //  inv_param.tol_offset[i] = inv_param.tol;
  //  inv_param.tol_hq_offset[i] = inv_param.tol_hq;
  //}

  // This is for Quda's sophisticated reliable update. 0.1 should be good.
  inv_param.reliable_delta = 0.1;
  inv_param.use_alternative_reliable = true;
  inv_param.use_sloppy_partial_accumulator = 0;
  inv_param.solution_accumulator_pipeline = 1;
  inv_param.max_res_increase = 1;

  // domain decomposition preconditioner parameters
  // inv_param.inv_type_precondition = precon_type;

  //inv_param.schwarz_type = precon_schwarz_type;
  //inv_param.precondition_cycle = precon_schwarz_cycle;
  //inv_param.tol_precondition = tol_precondition;
  //inv_param.maxiter_precondition = maxiter_precondition;
  //inv_param.omega = 1.0;

  inv_param.input_location  = QUDA_CPU_FIELD_LOCATION;
  inv_param.output_location = QUDA_CPU_FIELD_LOCATION;
  //inv_param.input_location  = QUDA_CUDA_FIELD_LOCATION;
  //inv_param.output_location = QUDA_CUDA_FIELD_LOCATION;

  // QUDA_DEBUG_VERBOSE is too nasty.

  inv_param.extlib_type = QUDA_EIGEN_EXTLIB;

  // Whether or not to use native BLAS LAPACK
  //inv_param.native_blas_lapack = (native_blas_lapack ? QUDA_BOOLEAN_TRUE : QUDA_BOOLEAN_FALSE);
  inv_param.native_blas_lapack = QUDA_BOOLEAN_TRUE;
  ///inv_param.native_blas_lapack = QUDA_BOOLEAN_FALSE;

  //// Whether or not use fused kernels for Mobius
  ////inv_param.use_mobius_fused_kernel = use_mobius_fused_kernel ? QUDA_BOOLEAN_TRUE : QUDA_BOOLEAN_FALSE;
  //inv_param.use_mobius_fused_kernel = QUDA_BOOLEAN_FALSE;


  ///////===check this variable
  std::array<int, 4> grid_partition = {1, 1, 1, 1};
  inv_param.split_grid[0] = grid_partition[0];
  inv_param.split_grid[1] = grid_partition[1];
  inv_param.split_grid[2] = grid_partition[2];
  inv_param.split_grid[3] = grid_partition[3];

  inv_param.struct_size = sizeof(inv_param);

  ////===END of Inv parameters

  alloc_csfield_cpu();
  alloc_csfield_gpu();

}

////0, double to single, 1 single to half, 10 double to double, 11 single to single, 12 half to half
inline void quda_inverter::setup_inv_param_prec(int prec_type)
{
  TIMER("setup_inv_param_prec");
  inv_param.cpu_prec                      = QUDA_DOUBLE_PRECISION;
  if(prec_type == 0)
  {
    inv_param.cuda_prec                     = QUDA_DOUBLE_PRECISION;
    inv_param.cuda_prec_sloppy              = QUDA_SINGLE_PRECISION;
    inv_param.cuda_prec_refinement_sloppy   = QUDA_SINGLE_PRECISION;
  }

  if(prec_type == 1)
  {
    inv_param.cuda_prec                     = QUDA_SINGLE_PRECISION;
    inv_param.cuda_prec_sloppy              = QUDA_HALF_PRECISION;
    inv_param.cuda_prec_refinement_sloppy   = QUDA_HALF_PRECISION;
  }

  if(prec_type == 2)
  {
    inv_param.cuda_prec                     = QUDA_DOUBLE_PRECISION;
    inv_param.cuda_prec_sloppy              = QUDA_HALF_PRECISION;
    inv_param.cuda_prec_refinement_sloppy   = QUDA_HALF_PRECISION;
  }

  
  if(prec_type == 10)
  {
    inv_param.cuda_prec                     = QUDA_DOUBLE_PRECISION;
    inv_param.cuda_prec_sloppy              = QUDA_DOUBLE_PRECISION;
    inv_param.cuda_prec_refinement_sloppy   = QUDA_DOUBLE_PRECISION;
  }
 
  if(prec_type == 11)
  {
    inv_param.cuda_prec                     = QUDA_SINGLE_PRECISION;
    inv_param.cuda_prec_sloppy              = QUDA_SINGLE_PRECISION;
    inv_param.cuda_prec_refinement_sloppy   = QUDA_SINGLE_PRECISION;
  }

  if(prec_type == 12)
  {
    inv_param.cuda_prec                     = QUDA_HALF_PRECISION;
    inv_param.cuda_prec_sloppy              = QUDA_HALF_PRECISION;
    inv_param.cuda_prec_refinement_sloppy   = QUDA_HALF_PRECISION;
  }

  if( gauge_param.cuda_prec != inv_param.cuda_prec or gauge_param.cuda_prec_sloppy != inv_param.cuda_prec_sloppy)
  {
    qassert(quda_gf_default.size() != 0);
    gauge_param.cuda_prec              = inv_param.cuda_prec;
    gauge_param.cuda_prec_sloppy       = inv_param.cuda_prec_sloppy;
    //gauge_param.cuda_prec_precondition = inv_param.cuda_prec_sloppy;
    //gauge_param.cuda_prec_eigensolver  = inv_param.cuda_prec_sloppy;

    //////gauge_param.cpu_prec               = QUDA_DOUBLE_PRECISION;
    //////gauge_param.cuda_prec              = QUDA_DOUBLE_PRECISION;

    //setup_gauge_param(gauge_param.t_boundary);
    //qassert(fermion_type == 1);
    //freeGaugeQuda();
    setup_link(&quda_gf_default[0], 0);
    alloc_csfield_gpu();
    CG_reset = true;
    setup_mat_mass(mass_mat, true);
  }
}

inline void quda_inverter::clear_mat()
{
  TIMER("clear_mat");
  if(dirac != NULL){delete dirac;dirac=NULL;}
  if(dirac_cg != NULL){delete dirac_cg;dirac_cg=NULL;}
  if(dirac_pc != NULL){delete dirac_pc;dirac_pc=NULL;}
  if(dSloppy != NULL){delete dSloppy;dSloppy=NULL;}
  if(dPre != NULL){delete dPre;dPre=NULL;}
  if(dEig != NULL){delete dEig;dEig=NULL;}

  if(mat       != NULL){delete mat      ;  mat       = NULL;}
  if(mat_pc    != NULL){delete mat_pc   ;  mat_pc    = NULL;}
  if(mat_Mdag  != NULL){delete mat_Mdag ;  mat_Mdag  = NULL;}
  if(mat_MMdag != NULL){delete mat_MMdag;  mat_MMdag = NULL;}
  if(mat_MdagM != NULL){delete mat_MdagM;  mat_MdagM = NULL;}

  if(m_cg != NULL){delete m_cg;  m_cg = NULL;}
  if(mSloppy != NULL){delete mSloppy;  mSloppy = NULL;}
  if(mPre != NULL){delete mPre;  mPre = NULL;}
  if(mEig != NULL){delete mEig;  mEig = NULL;}

  mat_E = NULL;
  clear_CG();
}

inline void quda_inverter::setup_inv_mass(const double mass)
{
  TIMER("setup_inv_mass");
  int verbos = 0;
  std::string val = qlat::get_env(std::string("qlat_quda_verbos"));
  if(val != ""){verbos = stringtonum(val);}
  if(verbos == -1)
  {
    inv_param.verbosity   = QUDA_SILENT;
    setVerbosity(QUDA_SILENT);
  }

  if(verbos == 0)
  {
    inv_param.verbosity   = QUDA_SUMMARIZE;
  }
  if(verbos == 1)
  {
    setVerbosity(QUDA_VERBOSE);
    inv_param.verbosity   = QUDA_VERBOSE;
  }

  if(verbos == 2)
  {
    setVerbosity(QUDA_DEBUG_VERBOSE);
    inv_param.verbosity   = QUDA_VERBOSE;
  }

  if(fermion_type == 0)
  {
    //inv_param.kappa = 0.130;
    //inv_param.mass = 0.5 / kappa - (1.0 + 3.0 / anisotropy);
    double anisotropy = gauge_param.anisotropy;
    inv_param.mass = mass;
    inv_param.kappa = 0.5 / (mass + (1.0 + 3.0 / anisotropy));
    ////double clover_csw setup with clover
    inv_param.clover_coeff = inv_param.clover_csw * inv_param.kappa;
    ////if(quda::comm_rank()== 0)printfQuda("Kappa = %.8f Mass = %.8f\n", inv_param.kappa, inv_param.mass);
    return ;
  }

  if(fermion_type == 1){inv_param.mass = mass;return ;}

  errorQuda("Fermion type not found!\n");

}

inline void quda_inverter::setup_mat_mass(const double mass, const bool force_do)
{
  TIMER("setup_mat_mass");
  int flag_do = 0;
  if(mat == NULL){flag_do = 1;}
  if(std::fabs(mass_mat - mass) > 1e-15){flag_do = 1;}
  if(force_do == true){flag_do = 1;}
  if(flag_do == 0){return ;}

  setup_inv_mass(mass);
  mass_mat = mass;

  /////print0("requested precision %d\n",inv_param.cuda_prec);
  //createDiracWithEig(dirac, dSloppy, dPre, dEig, inv_param, pc_solve);
  //createDirac(dirac, dSloppy, dPre, inv_param, pc_solve);

  //QudaSolveType;
  //QudaSolutionType
  clear_mat();
  //bool pc_solve = (inv_param.solve_type == QUDA_DIRECT_PC_SOLVE) ||
  //  (inv_param.solve_type == QUDA_NORMOP_PC_SOLVE) || (inv_param.solve_type == QUDA_NORMERR_PC_SOLVE);
  bool pc_solve = false;

  quda::DiracParam diracParam;
  setDiracParam(diracParam, &inv_param, pc_solve);

  //diracParam.tmp1 = gtmp1;
  //diracParam.tmp2 = gtmp2;

  dirac    = quda::Dirac::create(diracParam);

  setDiracParam(diracParam, &inv_param, true);
  dirac_pc = quda::Dirac::create(diracParam);

  mat        = new quda::DiracM(*dirac);
  mat_pc     = new quda::DiracM(*dirac_pc);
  mat_MdagM  = new quda::DiracMdagM(dirac);
  mat_MMdag  = new quda::DiracMMdag(*dirac);
  mat_Mdag   = new quda::DiracMdag(*dirac);

  ///CG related matrix
  {
    bool pc_solve = (inv_param.solve_type == QUDA_DIRECT_PC_SOLVE) ||
      (inv_param.solve_type == QUDA_NORMOP_PC_SOLVE) || (inv_param.solve_type == QUDA_NORMERR_PC_SOLVE);
    createDiracWithEig(dirac_cg, dSloppy, dPre, dEig, inv_param, pc_solve);
    m_cg       = new quda::DiracM(*dirac_cg);
    mSloppy    = new quda::DiracM(*dSloppy);
    mPre       = new quda::DiracM(*dPre);
    mEig       = new quda::DiracM(*dEig);
    CG_reset = true;
  }

  //DiracParam diracParam;
  //setDiracParam(diracParam, &inv_param, pc_solve);
  //dirac  = Dirac::create(diracParam);
}


inline void quda_inverter::setup_inc_eigencg(const int n_ev, const int n_kr, const int n_conv, const int df_grid, const double tol, const double inc_tol, const double tol_restart, const int restart_n, const int pipeline, const int inv_type)
{
  /////// inv_param.solve_type = QUDA_NORMOP_SOLVE;
  /////// inv_param.solve_type = QUDA_DIRECT_SOLVE;
  ///inv_param.inv_type = QUDA_CG_INVERTER;
  if(inv_type == 0){inv_param.inv_type = QUDA_EIGCG_INVERTER    ;inv_param.solve_type = QUDA_DIRECT_PC_SOLVE;}
  //if(inv_type == 0){inv_param.inv_type = QUDA_EIGCG_INVERTER    ;inv_param.solve_type = QUDA_NORMOP_SOLVE;}
  //if(inv_type == 1){inv_param.inv_type = QUDA_INC_EIGCG_INVERTER;inv_param.solve_type = QUDA_NORMOP_PC_SOLVE;}
  if(inv_type == 1){inv_param.inv_type = QUDA_INC_EIGCG_INVERTER;inv_param.solve_type = QUDA_NORMOP_SOLVE;}
  if(inv_type == 2){inv_param.inv_type = QUDA_INC_EIGCG_INVERTER;inv_param.solve_type = QUDA_DIRECT_SOLVE;}
  if(inv_type == 3){inv_param.inv_type = QUDA_INC_EIGCG_INVERTER;inv_param.solve_type = QUDA_DIRECT_PC_SOLVE;}
  if(inv_type == 4){inv_param.inv_type = QUDA_INC_EIGCG_INVERTER;inv_param.solve_type = QUDA_NORMOP_PC_SOLVE;}
  if(inv_type == 5){inv_param.inv_type = QUDA_INC_EIGCG_INVERTER;inv_param.solve_type = QUDA_NORMERR_PC_SOLVE;}
  //if(inv_type == 2){inv_param.inv_type = QUDA_GMRESDR_INVERTER ;inv_param.solve_type = QUDA_NORMOP_SOLVE;}
  //if(inv_type == 2){inv_param.inv_type = QUDA_GMRESDR_INVERTER ;inv_param.solve_type = QUDA_NORMOP_SOLVE;}
  //if(inv_type == 3){inv_param.inv_type = QUDA_FGMRESDR_INVERTER;inv_param.solve_type = QUDA_NORMOP_SOLVE;}
  //inv_type_precondition == QUDA_CG_INVERTER;

  //if(fermion_type == 0)inv_param.solve_type = QUDA_NORMOP_PC_SOLVE;
  //if(fermion_type == 1)inv_param.solve_type = QUDA_NORMOP_SOLVE;
  
  inv_param.use_init_guess = QUDA_USE_INIT_GUESS_NO;
  inv_param.inc_tol= inc_tol;
  if(pipeline ==  0){inv_param.pipeline = n_ev;}
  else{              inv_param.pipeline = pipeline;}
  

  ////additional inv_param
  inv_param.rhs_idx = 0;
  inv_param.n_ev            = n_ev;
  inv_param.max_search_dim  = n_kr;
  inv_param.deflation_grid  = df_grid;
  //inv_param.deflation_grid  = 16;
  //inv_param.deflation_grid  = n_ev;
  inv_param.tol_restart     = tol_restart;
  //inv_param.tol_restart     = inc_tol*1e-2;
  ////inv_param.tol_restart     = 5e+3*1e-7;

  inv_param.eigcg_max_restarts = restart_n;
  inv_param.max_restart_num    = restart_n;

  inv_param.eigenval_tol = tol;
  //inv_param.eigenval_tol = inc_tol*1e2;
  //inv_param.inc_tol = inv_param.inc_tol;
  //inv_param.eigenval_tol = 1e-1;
  //inv_param.eigenval_tol = tol*1e2;

  // domain decomposition preconditioner parameters
  inv_param.schwarz_type = QUDA_INVALID_SCHWARZ;
  inv_param.accelerator_type_precondition = QUDA_INVALID_ACCELERATOR;
  inv_param.precondition_cycle = 1;
  ////inv_param.tol_precondition = tol;
  inv_param.tol_precondition = 1e-2;
  inv_param.maxiter_precondition = 4;
  inv_param.omega = 1.0;

  inv_param.gcrNkrylov = 6;
  inv_param.inv_type_precondition = QUDA_INVALID_INVERTER;
  //inv_param.inv_type_precondition = QUDA_CG_INVERTER;
  //inv_param.inv_type_precondition = QUDA_MG_INVERTER;
  //inv_param.inv_type_precondition = QUDA_SD_INVERTER;
  inv_param.extlib_type = QUDA_EIGEN_EXTLIB;

  if(inc_tol > 1e-7){
    inv_param.cuda_prec_eigensolver         = QUDA_SINGLE_PRECISION;
    inv_param.cuda_prec_precondition        = QUDA_SINGLE_PRECISION;
    inv_param.clover_cuda_prec_precondition = QUDA_SINGLE_PRECISION;
    inv_param.clover_cuda_prec_eigensolver  = QUDA_SINGLE_PRECISION;

    inv_param.cuda_prec_sloppy              = QUDA_SINGLE_PRECISION;
    inv_param.clover_cuda_prec_sloppy       = QUDA_SINGLE_PRECISION;

    gauge_param.cuda_prec_sloppy            = QUDA_SINGLE_PRECISION;
    gauge_param.cuda_prec_precondition      = QUDA_SINGLE_PRECISION;
    gauge_param.cuda_prec_eigensolver       = QUDA_SINGLE_PRECISION;

    //inv_param.cuda_prec_refinement_sloppy   = QUDA_SINGLE_PRECISION;
    //inv_param.clover_cuda_prec_refinement_sloppy = QUDA_SINGLE_PRECISION;
  }else{
    inv_param.cuda_prec_eigensolver         = QUDA_DOUBLE_PRECISION;
    inv_param.cuda_prec_precondition        = QUDA_DOUBLE_PRECISION;
    inv_param.clover_cuda_prec_precondition = QUDA_DOUBLE_PRECISION;
    inv_param.clover_cuda_prec_eigensolver  = QUDA_DOUBLE_PRECISION;
    gauge_param.cuda_prec_precondition      = QUDA_DOUBLE_PRECISION;
    gauge_param.cuda_prec_eigensolver       = QUDA_DOUBLE_PRECISION;


    inv_param.cuda_prec_sloppy              = QUDA_DOUBLE_PRECISION;
    inv_param.clover_cuda_prec_sloppy       = QUDA_DOUBLE_PRECISION;
    gauge_param.cuda_prec_sloppy            = QUDA_DOUBLE_PRECISION;

    //inv_param.cuda_prec_sloppy              = QUDA_SINGLE_PRECISION;
    //inv_param.clover_cuda_prec_sloppy       = QUDA_SINGLE_PRECISION;
    //gauge_param.cuda_prec_sloppy            = QUDA_SINGLE_PRECISION;

    //inv_param.cuda_prec_refinement_sloppy   = QUDA_DOUBLE_PRECISION;
    //inv_param.clover_cuda_prec_refinement_sloppy = QUDA_DOUBLE_PRECISION;

    //inv_param.cuda_prec_sloppy              = QUDA_SINGLE_PRECISION;
    //inv_param.cuda_prec_refinement_sloppy   = QUDA_SINGLE_PRECISION;
    //inv_param.clover_cuda_prec_sloppy       = QUDA_SINGLE_PRECISION;
    //inv_param.clover_cuda_prec_refinement_sloppy = QUDA_SINGLE_PRECISION;

  }


  inv_param.struct_size = sizeof(inv_param);

  ////clear_mat();
  alloc_csfield_cpu();
  alloc_csfield_gpu();

  //cs_cpu.print();
  //cs_gpu.print();

  eig_param = newQudaEigParam();
  eig_param.preserve_deflation = QUDA_BOOLEAN_TRUE;

  eig_param.invert_param = &inv_param;

  eig_param.import_vectors = QUDA_BOOLEAN_FALSE;
  eig_param.run_verify = QUDA_BOOLEAN_FALSE;

  strcpy(eig_param.vec_infile, "");
  strcpy(eig_param.vec_outfile, "");
  eig_param.io_parity_inflate = QUDA_BOOLEAN_FALSE;

  eig_param.extlib_type = QUDA_EIGEN_EXTLIB;

  /////TODO mixed precision
  //eig_param.cuda_prec_ritz =  QUDA_SINGLE_PRECISION;
  if(inc_tol > 1e-7){
  eig_param.cuda_prec_ritz =  QUDA_SINGLE_PRECISION;
  inv_param.cuda_prec_ritz =  QUDA_SINGLE_PRECISION;
  }else{
  eig_param.cuda_prec_ritz =  QUDA_DOUBLE_PRECISION;
  inv_param.cuda_prec_ritz =  QUDA_DOUBLE_PRECISION;}
  //eig_param.cuda_prec_ritz =  QUDA_DOUBLE_PRECISION;
  //if(tol > 1e-6){eig_param.cuda_prec_ritz = QUDA_SINGLE_PRECISION;}
  //else{eig_param.cuda_prec_ritz =  QUDA_DOUBLE_PRECISION;}
  //eig_param.cuda_prec_ritz = QUDA_DOUBLE_PRECISION;
  eig_param.location       = QUDA_CUDA_FIELD_LOCATION;
  eig_param.mem_type_ritz  = QUDA_MEMORY_DEVICE;

  eig_param.n_ev   = n_ev;
  eig_param.n_kr   = n_kr;
  if(n_conv == 0){eig_param.n_conv = n_conv;}
  else{           eig_param.n_conv = n_kr + n_ev;}
  eig_param.tol    = tol;

  eig_param.max_restarts     = inv_param.eigcg_max_restarts;

  eig_param.n_ev_deflate = eig_param.n_conv;
  eig_param.require_convergence = QUDA_BOOLEAN_TRUE;
  ////eig_param.require_convergence = QUDA_BOOLEAN_FALSE;

  eig_param.nk  = eig_param.n_ev;
  eig_param.np  = eig_param.n_ev * inv_param.deflation_grid;

  if(df_preconditioner != NULL){destroyDeflationQuda(df_preconditioner);df_preconditioner=NULL;}
  df_preconditioner  = newDeflationQuda(&eig_param);
  inv_param.deflation_op   = df_preconditioner;

}

inline void quda_inverter::setup_eigen(const double mass, const int num_eigensys, const double err, const int eig_poly_deg, const double eig_amin, const bool compute, const int nkr, const double eig_amax, const double qr_tol, const int eig_check_interval, const int eig_max_restarts, const int eig_batched_rotate )
{
  TIMER("setup_eigen");
  /////may need settings
  nvec = num_eigensys;
  if(nvec == 0){return ;}
  use_eigen_pc = 1;
  /////mass_eig = mass;

  int eig_n_kr = nkr;
  if(nkr <= 0){eig_n_kr = 2*nvec;}
  double eig_tol    = err;
  //double eig_qr_tol = err*0.1;
  double eig_qr_tol = err*qr_tol;
  //int eig_batched_rotate = 0; // If unchanged, will be set to maximum
  ////int eig_check_interval = eig_check_interval;
  ///int eig_max_restarts = 10000;
  bool eig_use_eigen_qr = true;
  bool eig_use_poly_acc = true;
  ///int eig_poly_deg = 100;
  ///double eig_amin = 0.1;
  ///double eig_amax = 0.0; // If zero is passed to the solver, an estimate will be computed

  ////preconditionor for the inverter

  inv_param.cuda_prec_precondition        = QUDA_DOUBLE_PRECISION;
  inv_param.cuda_prec_eigensolver         = QUDA_DOUBLE_PRECISION;
  inv_param.clover_cuda_prec_precondition = QUDA_DOUBLE_PRECISION;
  inv_param.clover_cuda_prec_eigensolver  = QUDA_DOUBLE_PRECISION;
  gauge_param.cuda_prec_precondition = QUDA_DOUBLE_PRECISION;
  gauge_param.cuda_prec_eigensolver  = QUDA_DOUBLE_PRECISION;

  //gauge_param.cuda_prec_sloppy       = QUDA_SINGLE_PRECISION;

  //gauge_param.cuda_prec_sloppy       = QUDA_DOUBLE_PRECISION;
  //inv_param.cuda_prec_sloppy              = QUDA_DOUBLE_PRECISION;
  //inv_param.clover_cuda_prec_sloppy       = QUDA_DOUBLE_PRECISION;

  setup_inv_param_prec(0);
  //setup_inv_param_prec(10);
  setup_mat_mass(mass);
  alloc_csfield_cpu();
  alloc_csfield_gpu();

  inv_param.use_init_guess = QUDA_USE_INIT_GUESS_YES;

  if(nvec <= 0){errorQuda("Eigensystem need nvec largger than zero");}
  if(quda::comm_rank()== 0){printfQuda("Number of QUDA eigen vectors %d .\n", nvec);}
  eig_param = newQudaEigParam();
  eig_param.invert_param = &inv_param;

  ////===basice eig parameters
  //QUDA_EIG_TR_LANCZOS,     // Thick restarted lanczos solver
  //QUDA_EIG_BLK_TR_LANCZOS, // Block Thick restarted lanczos solver
  //QUDA_EIG_IR_ARNOLDI,     // Implicitly Restarted Arnoldi solver
  //QUDA_EIG_BLK_IR_ARNOLDI, // Block Implicitly Restarted Arnoldi solver
  int eigensolve_type = 0;
  std::string val = qlat::get_env(std::string("qlat_quda_eigensolve_type"));
  if(val != ""){eigensolve_type = stringtonum(val);}
  if(eigensolve_type == 0){eig_param.eig_type = QUDA_EIG_TR_LANCZOS; } // Thick restarted lanczos solver
  if(eigensolve_type == 1){eig_param.eig_type = QUDA_EIG_BLK_TR_LANCZOS; } //Block Thick restarted lanczos solver
  if(eigensolve_type == 2){eig_param.eig_type = QUDA_EIG_IR_ARNOLDI;} // Implicitly Restarted Arnoldi solver
  if(eigensolve_type == 3){eig_param.eig_type = QUDA_EIG_BLK_IR_ARNOLDI;}  // Block Implicitly Restarted Arnoldi solver

  eig_param.spectrum = QUDA_SPECTRUM_SR_EIG;
  if ((eig_param.eig_type == QUDA_EIG_TR_LANCZOS || eig_param.eig_type == QUDA_EIG_BLK_TR_LANCZOS)
      && !(eig_param.spectrum == QUDA_SPECTRUM_LR_EIG || eig_param.spectrum == QUDA_SPECTRUM_SR_EIG)) {
    errorQuda("Only real spectrum type (LR or SR) can be passed to Lanczos type solver.");
  }

  // The solver will exit when n_conv extremal eigenpairs have converged
  eig_param.n_conv       = nvec;
  // Inverters will deflate only this number of vectors.
  eig_param.n_ev_deflate = nvec;

  //eig_param.block_size
  //  = (eig_param.eig_type == QUDA_EIG_TR_LANCZOS || eig_param.eig_type == QUDA_EIG_IR_ARNOLDI) ? 1 : eig_block_size;
  eig_param.block_size = 1;

  eig_param.n_ev = nvec;
  eig_param.n_kr = eig_n_kr;
  eig_param.tol  = eig_tol;
  eig_param.qr_tol = eig_qr_tol;
  eig_param.batched_rotate = eig_batched_rotate;

  eig_param.require_convergence = QUDA_BOOLEAN_TRUE;
  //if(eig_max_restarts < 10000){
  //  eig_param.require_convergence = QUDA_BOOLEAN_FALSE;
  //}
  eig_param.check_interval = eig_check_interval;
  eig_param.max_restarts = eig_max_restarts;

  //setEigParam(eig_param);
  //eig_param.use_norm_op = QUDA_BOOLEAN_TRUE;
  //eig_param.use_dagger  = QUDA_BOOLEAN_TRUE;

  ////** What type of Dirac operator we are using **/
  ////** If !(use_norm_op) && !(use_dagger) use M. **/
  ////** If use_dagger, use Mdag **/
  ////** If use_norm_op, use MdagM **/
  ////** If use_norm_op && use_dagger use MMdag. **/

  eig_param.use_norm_op = QUDA_BOOLEAN_TRUE;
  ////eig_param.use_dagger  = QUDA_BOOLEAN_TRUE;
  eig_param.use_dagger  = QUDA_BOOLEAN_FALSE;

  eig_param.compute_gamma5  = QUDA_BOOLEAN_FALSE;
  eig_param.compute_svd     = QUDA_BOOLEAN_FALSE;
  eig_param.arpack_check    = QUDA_BOOLEAN_FALSE;

  if (eig_param.compute_svd) {
    eig_param.use_dagger = QUDA_BOOLEAN_FALSE;
    eig_param.use_norm_op = QUDA_BOOLEAN_TRUE;
  }

  eig_param.use_eigen_qr = eig_use_eigen_qr ? QUDA_BOOLEAN_TRUE : QUDA_BOOLEAN_FALSE;
  eig_param.use_poly_acc = eig_use_poly_acc ? QUDA_BOOLEAN_TRUE : QUDA_BOOLEAN_FALSE;
  eig_param.poly_deg = eig_poly_deg;
  eig_param.a_min = eig_amin;
  eig_param.a_max = eig_amax;

  eig_param.arpack_check = QUDA_BOOLEAN_FALSE;

  strcpy(eig_param.vec_infile, "");
  strcpy(eig_param.vec_outfile, "");
  //eig_param.save_prec = eig_save_prec;
  bool eig_io_parity_inflate = false;
  eig_param.io_parity_inflate = eig_io_parity_inflate ? QUDA_BOOLEAN_TRUE : QUDA_BOOLEAN_FALSE;

  eig_param.struct_size = sizeof(eig_param);
  /////===END of eig_param

  ///evecs.resize(nvec);

  ///for (int i = 0; i < nvec; i++) {evecs[i].resize(gsrc->Volume() * spinor_site_size);}

  //ColorSpinorParam cpuParam(&evecs[0][0], inv_param, &X[0], inv_param.solution_type, inv_param.input_location);
  //for (int i = 0; i < num_eigensys; i++) {
  //  cpuParam.v = &evecs[i][0];
  //  evecs_.push_back(ColorSpinorField::Create(cpuParam));
  //}

  /////singleE = single;
  // If you attempt to compute part of the imaginary spectrum of a symmetric matrix,
  // the solver will fail.
  if ((eig_param.spectrum == QUDA_SPECTRUM_LI_EIG || eig_param.spectrum == QUDA_SPECTRUM_SI_EIG)
      && ((eig_param.use_norm_op || (inv_param.dslash_type == QUDA_LAPLACE_DSLASH))
          || ((inv_param.dslash_type == QUDA_STAGGERED_DSLASH || inv_param.dslash_type == QUDA_ASQTAD_DSLASH)
              && inv_param.solve_type == QUDA_DIRECT_PC_SOLVE))) {
    errorQuda("Cannot compute imaginary spectra with a hermitian operator");
  }
  // Gamma5 pre-multiplication is only supported for the M type operator
  if (eig_param.compute_gamma5) {
    if (eig_param.use_norm_op || eig_param.use_dagger) {
      errorQuda("gamma5 premultiplication is only supported for M type operators: dag = %s, normop = %s",
                eig_param.use_dagger ? "true" : "false", eig_param.use_norm_op ? "true" : "false");
    }
  }

  ///gtmp1 = quda::ColorSpinorField::Create(cs_gpu);
  ///d.prepare(in_b, out_b, *gtmp0, *gtmp1, inv_param.solution_type);
  if(fermion_type == 0){mat_E = mat_MMdag;}
  if(fermion_type == 1){mat_E = mat_pc   ;}

  if(compute){
    /////evecs = (void **)safe_malloc(nvec * sizeof(void *));
    //bool singleE = false;
    //if(compute == true ){singleE = false;}
    //if(compute == false){singleE = true;}
    evalsK.resize(nvec, 0.0);

    ////for (int i = 0; i < kSpace_cpu.size(); i++) delete kSpace_cpu[i];kSpace_cpu.resize(0);
    quda::ColorSpinorParam cs0 = quda::ColorSpinorParam(cs_gpuD);
    cs0.is_composite  = false;cs0.is_component  = false;
    kSpace.resize(nvec);
    //for (int i = 0; i < nvec; i++){kSpace.push_back(quda::ColorSpinorField::Create(cs_gpuD));}
    for (int i = 0; i < nvec; i++){kSpace[i] = quda::ColorSpinorField(cs0);}
    fSpace.resize(0);evalsF.resize(0);
    //for (int i = 0; i < nvec; i++) { 
    //  if(singleE== false)kSpace.push_back(quda::ColorSpinorField::Create(cs_gpuD)); 
    //  if(singleE== true )kSpace.push_back(quda::ColorSpinorField::Create(cs_gpuF)); 
    //}

    eig_solveK = quda::EigenSolver::create(&eig_param, *mat_E, profileEigensolve);
    (*eig_solveK)(kSpace, evalsK);

    ////eig_solve->printEigensolverSetup();
    //eig_solve->computeEvals(*mat, kSpace, evals, eig_param.n_conv);
    ////printf("===Deflation size n_ev_deflate %d, n_conv %d \n", eig_param->n_ev_deflate, eig_param->n_conv );
    //eig_solve->orthoCheck(kSpace, eig_param.n_ev_deflate);
    ////eig_solve->deflate(*tmp_out, *tmp_in, kSpace, evals, true);
    ////copy vectors to host
    ////for (int i = 0; i < eig_param.n_conv; i++) *evecs_[i] = *kSpace[i];
    evals_ZERO.resize(evalsK.size());
    mass_value = 0.0;
    for(int ni=0;ni<evals_ZERO.size();ni++)
    {
      evals_ZERO[ni] = evalsK[ni].real()/1.0 - 4.0 * mass * mass;
    }
    /////evals_ERR = (*eig_solveK).residua;
    evals_ERR.resize(evalsK.size(), 0.0);

    //for (int i = 0; i < kSpace.size(); i++) delete kSpace[i];kSpace.resize(0);
    //for(int i=0;i<nvec;i++)
    //{
    //  kSpace.push_back(quda::ColorSpinorField::Create(cs_gpuD));
    //  *kSpace[i] = *kSpace_cpu[i];
    //}

    ////copy to GPU float and stuff, assummed all double
  }

}

inline void quda_inverter::update_eigen_mass(const double mass, bool force)
{
  TIMER("update_eigen_mass");
  if(mass_value != mass or force)
  {
    qassert(evals_ZERO.size() == evalsK.size() + evalsF.size());
    int n0  = evalsK.size();
    int n1  = evalsF.size();
    int nvec = n0+n1;
    evalsZ.resize(nvec);
    for(int ni=0;ni<nvec;ni++)
    {
      quda::Complex tmp = quda::Complex(evals_ZERO[ni].real() + 4.0 * mass * mass, 0.0);
      if(ni <  n0){evalsK[ni     ] = tmp;}
      if(ni >= n0){evalsF[ni - n0] = tmp;}
      evalsZ[ni] = tmp;
    }
  }
  mass_value = mass;
}

inline void quda_inverter::random_src(const int seed)
{
  for(int i=0;i<int(seed)%20 + 20*quda::comm_rank_global();i++){quda::comm_drand();}
  int random_mode = 1;
  random_Ty((qlat::Complex*) gsrc->V(), gsrc->Volume() * spinor_site_size, 1, seed + 111111, random_mode);
  quda::blas::ax(0.05, *gsrc);
  quda::Complex* tmp = (quda::Complex*) (gsrc->V());
  long totalN = gsrc->Volume() * spinor_site_size;
  //for(long i=0;i<totalN/200 + 1;i++)
  //for(long i=0;i< 50;i++)
  //{
  //  long vi = long(quda::comm_drand()*totalN);
  //  double ri = quda::comm_drand()*totalN;
  //  tmp[vi] = ri * quda::Complex(quda::comm_drand(), quda::comm_drand());
  //}
}

/////reconstruct and push_back to Fspace with double prec
inline void quda_inverter::reconstruct_full(const double mass)
{
  TIMER("reconstruct_full");
  std::vector<quda::Complex  >& vals = evalsZ;
  if(use_eigen_pc == 0 or nvec <= 0){
    ////for (int i = 0; i < ZSpace.size(); i++){delete ZSpace[i];}
    ZSpace.resize(0); evalsZ.resize(0);
    return;
  }
  qassert(kSpace.size() + fSpace.size() == nvec);
  const int off = kSpace.size();
  quda::Complex Im = quda::Complex(0.0, 1.0);
  double m = mass;
  if(mass == -1){m = inv_param.mass;}

  vals.resize(2 * nvec);

  quda::ColorSpinorField* src = NULL;
  quda::Complex           lab = quda::Complex(0.0, 0.0);
  quda::ColorSpinorField* Czero;
  quda::ColorSpinorParam cs0 = quda::ColorSpinorParam(cs_gpu);
  quda::ColorSpinorParam csD = quda::ColorSpinorParam(cs_gpuD);
  cs0.is_composite  = false;cs0.is_component  = false;
  csD.is_composite  = false;csD.is_component  = false;

  Czero = quda::ColorSpinorField::Create(cs0);
  quda::blas::zero(*Czero);
  src = quda::ColorSpinorField::Create(csD);

  ZSpace.resize(2 * nvec);
  for(int n = 0; n < nvec; n++)
  { 
    if(n <  off){(*src) = (kSpace[n]      ); lab = evalsK[n].real();}
    if(n >= off){(*src) = (fSpace[n - off]); lab = evalsF[n-off].real();}
    lab = std::sqrt(lab.real()/1.0 - 4.0*m*m);

    ////ZSpace.push_back(quda::ColorSpinorField::Create(cs_gpu));
    ////ZSpace.push_back(quda::ColorSpinorField::Create(cs_gpu));
    ZSpace[n*2 + 0] = quda::ColorSpinorField(cs0);
    ZSpace[n*2 + 1] = quda::ColorSpinorField(cs0);
    quda::blas::zero((ZSpace[n*2 + 0]).Even());
    quda::blas::zero((ZSpace[n*2 + 1]).Even());
    quda::blas::caxpy(-1.0*Im*lab, *src, (ZSpace[n*2 + 0]).Even());
    quda::blas::caxpy(+1.0*Im*lab, *src, (ZSpace[n*2 + 1]).Even());

    /////Doe v_e
    dirac->Dslash((ZSpace[n*2 + 0]).Odd(), *src, QUDA_ODD_PARITY);
    (ZSpace[n*2 + 1]).Odd() = (ZSpace[n*2 + 0]).Odd();

    quda::blas::ax(-1.0/(std::sqrt(2)*lab.real()), ZSpace[n*2 + 0]);
    quda::blas::ax(-1.0/(std::sqrt(2)*lab.real()), ZSpace[n*2 + 1]);

    /////m + b |\lambda|
    vals[n*2 + 0] = 2*m + Im * lab; 
    vals[n*2 + 1] = 2*m - Im * lab; 
  }

  delete Czero;
  delete src;

  check_residualF();
}

inline void quda_inverter::check_residualF()
{
  TIMER("check_residualF");
  std::vector<quda::Complex  >& vals = evalsZ;
  quda::Complex n_unit(-1.0, 0.0);
  for(int n=0;n<nvec*2;n++)
  {   
    *gsrc = ZSpace[n];
    *gres = ZSpace[n];
    quda::blas::zero(*gtmp1);
    //(*mat)(*gtmp1, *gres, *gtmp0, *gtmp2);
    (*mat)(*gtmp1, *gres);

    quda::Complex srcn = quda::blas::norm2(*gsrc);
    quda::Complex resn = quda::blas::norm2(*gtmp1);
    quda::Complex evals  = quda::blas::cDotProduct(*gsrc, *gtmp1) / quda::blas::norm2(*gsrc);
    quda::Complex factor = sqrt(quda::blas::norm2(*gtmp1)) / sqrt(quda::blas::norm2(*gsrc));
    quda::blas::caxpby(evals, *gsrc , n_unit, *gtmp1 ); ///tmp = ev*src + n * gtmp
    quda::Complex residual = sqrt(quda::blas::norm2(*gtmp1)/ quda::blas::norm2(*gsrc));

    quda::blas::zero(*gtmp1);
    //(*mat)(*gtmp1, *gres, *gtmp0, *gtmp2);
    (*mat)(*gtmp1, *gres);
    quda::Complex even_v  = quda::blas::cDotProduct((*gsrc).Even(), (*gtmp1).Even()) / quda::blas::norm2((*gsrc).Even());
    quda::blas::caxpby(even_v, (*gsrc).Even() , n_unit, (*gtmp1).Even() );
    quda::Complex res_e = sqrt(quda::blas::norm2((*gtmp1).Even())/ quda::blas::norm2((*gsrc).Even()));

    quda::blas::zero(*gtmp1);
    //(*mat)(*gtmp1, *gres, *gtmp0, *gtmp2);
    (*mat)(*gtmp1, *gres);
    quda::Complex odd_v  = quda::blas::cDotProduct((*gsrc).Odd(), (*gtmp1).Odd()) / quda::blas::norm2((*gsrc).Odd());
    quda::blas::caxpby(odd_v, (*gsrc).Odd() , n_unit, (*gtmp1).Odd() );
    quda::Complex res_o = sqrt(quda::blas::norm2((*gtmp1).Odd())/ quda::blas::norm2((*gsrc).Odd()));

    if(quda::comm_rank_global()== 0){
      //printf("===vec %5d, v %+.1e %+.1e, e %+.1e %+.1e, residual %.3e, %.3e %.3e, %+.1e %+.1e %+.1e %+.1e \n", n, 
      //    residual.real(), vals[n].real(), vals[n].imag(), evals.real(), evals.imag(), res_e.real(), res_o.real(),
      //    even_v.real(), even_v.imag(), odd_v.real(), odd_v.imag() );
      printf("===vec %5d, v %+.1e %+.1e, e %+.1e %+.1e, residual %+.3e, %+.3e %+.3e \n", n, 
          vals[n].real(), vals[n].imag(), evals.real(), evals.imag(), residual.real(), res_e.real(), res_o.real() );
    }
  }
}

////from gsrc to gtmp2
inline void quda_inverter::prepare_low_prop(int mode )
{
  TIMER("prepare_low_prop");
  
  if(use_eigen_pc == 0 or nvec <= 0){quda::blas::zero(*gres);return;}
  if(mode == 1 and ZSpace.size() != nvec*2){qassert(false);}
  double m = inv_param.mass;
  update_eigen_mass(m, true);

  /////eigensystem reconstructed
  if(mode == 1){
    ////mode 1 write
    ///quda::ColorSpinorField& res = *gtmp2;
    quda::blas::zero(*gtmp2);

    // Perform Sum_i V_i * (L_i)^{-1} * (V_i)^dag * vec = vec_defl
    int n_defl = ZSpace.size();
    std::vector<quda::ColorSpinorField *> eig_vecs;
    eig_vecs.reserve(n_defl);
    for (int i = 0; i < n_defl; i++) eig_vecs.push_back(&ZSpace[i]);

    // 1. Take block inner product: (V_i)^dag * vec = A_i
    std::vector<quda::Complex> s(n_defl * 1);
    std::vector<quda::ColorSpinorField *> src_;src_.push_back(&(*gsrc));
    ///= const_cast<decltype(src) &>(src);
    quda::blas::cDotProduct(s.data(), eig_vecs, src_);

    // 2. Perform block caxpy: V_i * (L_i)^{-1} * A_i
    for (int i = 0; i < n_defl; i++) { s[i] /= evalsZ[i]; }

    // 3. Accumulate sum vec_defl = Sum_i V_i * (L_i)^{-1} * A_i
    //if (!accumulate)
    //  for (auto &x : sol) blas::zero(*x);
    std::vector<quda::ColorSpinorField *> sol;sol.push_back(&(*gtmp2));
    quda::blas::caxpy(s.data(), eig_vecs, sol);

    //////===check sections
    ///////cross check even parts
    //quda::ColorSpinorField *src;
    //quda::ColorSpinorField *sol0;
    //quda::ColorSpinorField *sol1;
    //(*gtmp1) = (*gsrc);
    //dirac_pc->prepare(src, sol0, (*gtmp0), (*gtmp1), QUDA_MAT_SOLUTION);
    //dirac_pc->prepare(src, sol1, (*gres ), (*gtmp1), QUDA_MAT_SOLUTION);
    //quda::blas::zero(*sol0);quda::blas::zero(*sol1);
    //if(kSpace.size()!=0){eig_solveK->deflate((*sol0) , (*src), kSpace, evalsK, false);}
    //if(fSpace.size()!=0){eig_solveF->deflate((*sol1) , (*src), fSpace, evalsF, false);}
    //quda::Complex lambda  = quda::Complex(1.0, 0.0);
    //if(kSpace.size()!=0){lambda  = lambda - quda::blas::cDotProduct(*sol0, *sol1) / quda::blas::norm2(*sol0);}
    //quda::blas::caxpy(lambda, *sol0, *sol1);

    //quda::Complex s0_e = quda::blas::norm2(gsrc->Even());
    //quda::Complex s0_o = quda::blas::norm2(gsrc->Odd());
    //quda::Complex n0_e = quda::blas::norm2(gtmp2->Even());
    //quda::Complex n0_o = quda::blas::norm2(gtmp2->Odd());

    //quda::Complex m_unit( 1.0, 0.0);
    //quda::Complex n_unit(-1.0, 0.0);
    //(*gtmp1) = *gtmp2;
    //quda::blas::caxpby(m_unit, (*gres).Even() , n_unit, (*gtmp1).Even());
    //quda::Complex residual = quda::blas::norm2((*gtmp1).Even());
    //if(quda::comm_rank_global()== 0)printf("===Even %.3e, s %.1e %.1e, n %.1e %.1e \n", residual.real(), 
    //  s0_e.real(), s0_o.real(), n0_e.real(), n0_o.real());
  }

  quda::Complex n_unit(1.0, 0.0);
  if(mode == 0){
    ////mode 0 write
    quda::blas::zero(*gres);
    int n_defl = 0;
    //*gtmp1 = *gsrc;
    /////Doe v_e
    quda::blas::zero((*gtmp1).Odd());
    dirac->Dslash((*gtmp1).Odd(), (*gsrc).Odd(), QUDA_EVEN_PARITY);
    quda::blas::ax(-1.0, (*gtmp1).Odd());
    (*gtmp1).Even() = (*gsrc).Even();

    if(gtmp1D == NULL){gtmp1D = new quda::ColorSpinorField(cs_gpuD);}
    if(gtmp2D == NULL){gtmp2D = new quda::ColorSpinorField(cs_gpuD);}
    if(gtmp1F == NULL){gtmp1F = new quda::ColorSpinorField(cs_gpuF);}
    if(gtmp2F == NULL){gtmp2F = new quda::ColorSpinorField(cs_gpuF);}
    //if(gtmp2D == NULL){gtmp2D = new quda::ColorSpinorField(cs_gpuD);}
    //if(gtmp2F == NULL){gtmp2F = new quda::ColorSpinorField(cs_gpuF);}

    for(int kf=0;kf<2;kf++)
    {
      std::vector<quda::ColorSpinorField *> eig_vecs;
      if(kf==0){n_defl = kSpace.size();eig_vecs.reserve(n_defl);for(int i=0;i<n_defl;i++){eig_vecs.push_back(&kSpace[i]);}}
      if(kf==1){n_defl = fSpace.size();eig_vecs.reserve(n_defl);for(int i=0;i<n_defl;i++){eig_vecs.push_back(&fSpace[i]);}}

      if(n_defl == 0){continue ;}
      std::vector<quda::Complex> A(n_defl);
      std::vector<quda::Complex> B(n_defl);

      // 1. Take block inner product: (V_i)^dag * vec = A_i
      std::vector<quda::ColorSpinorField *> buf;
      ////if(kf == 0){src_.push_back(&(gtmp1->Even()));}
      if(kf == 0){buf.push_back(gtmp1D);}
      if(kf == 1){buf.push_back(gtmp1F);}
      *buf[0] = gtmp1->Even();

      quda::blas::cDotProduct(A.data(), eig_vecs, buf);
      ////src_[0] = &(gtmp1->Odd());
      *buf[0] = gtmp1->Odd();
      quda::blas::cDotProduct(B.data(), eig_vecs, buf);
      quda::Complex ev;
      for (int i = 0; i < n_defl; i++) {
        if(kf==0){ev = evalsK[i];}
        if(kf==1){ev = evalsF[i];}
        quda::Complex l = std::sqrt(ev.real()/1.0 - 4.0*m*m);
        quda::Complex ai = A[i];
        quda::Complex bi = B[i];
        A[i] = ( 2*m * ai - bi ) / (4*m*m + l*l);
        B[i] = -1.0 * ai/(4.0*m*m + l*l) - 2*m * bi/(l*l * (4*m*m + l*l));
      }

      ////std::vector<quda::ColorSpinorField *> sol;
      //sol.push_back(&(gres->Even()));
      quda::blas::caxpy(A.data(), eig_vecs, buf);
      /////gres->Even() = gres->Even() + *buf[0];
      gtmp2->Even() = *buf[0];
      quda::blas::caxpby(n_unit, gtmp2->Even() , n_unit, gres->Even());
      ////sol[0] = &(gres->Odd());
      quda::blas::caxpy(B.data(), eig_vecs, buf);
      gtmp2->Odd()  = *buf[0];
      quda::blas::caxpby(n_unit, gtmp2->Odd()  , n_unit, gres->Odd());
      ////gres->Odd()  = gres->Odd() + *buf[0];
    }

    quda::blas::zero((*gtmp1).Odd());
    dirac->Dslash((*gtmp1).Odd(), (*gres).Odd(), QUDA_ODD_PARITY);
    quda::blas::ax(-1.0, (*gtmp1).Odd());
    (*gres).Odd() = (*gtmp1).Odd();

    ////////===check sections uncomment for test 
    //quda::Complex s0_e = quda::blas::norm2(gsrc->Even());
    //quda::Complex s0_o = quda::blas::norm2(gsrc->Odd());
    //quda::Complex n0_e = quda::blas::norm2(gtmp2->Even());
    //quda::Complex n0_o = quda::blas::norm2(gtmp2->Odd());
    //quda::Complex n1_e = quda::blas::norm2(gres->Even());
    //quda::Complex n1_o = quda::blas::norm2(gres->Odd());

    //quda::Complex m_unit( 1.0, 0.0);
    //quda::Complex n_unit(-1.0, 0.0);
    //(*gtmp0) =(*gtmp2);
    //quda::blas::caxpby(m_unit, (*gres).Even() , n_unit, (*gtmp0).Even());
    //quda::Complex res_e = quda::blas::norm2((*gtmp0).Even());
    //(*gtmp0) =(*gtmp2);
    //quda::blas::caxpby(m_unit, (*gres).Odd() , n_unit, (*gtmp0).Odd());
    //quda::Complex res_o = quda::blas::norm2((*gtmp0).Odd() );

    //if(quda::comm_rank_global()== 0)printf("===Even %.3e, Odd %.3e , s %.1e %.1e , n %.1e %.1e %.1e %.1e \n", res_e.real(), res_o.real(), 
    //    s0_e.real(), s0_o.real(), n0_e.real(), n0_o.real(), n1_e.real(), n1_o.real());
  }

  quda::saveTuneCache();
}

inline void quda_inverter::deflate(quda::ColorSpinorField &sol, const quda::ColorSpinorField &src, std::vector<quda::ColorSpinorField> &evecs, const std::vector<quda::Complex> &evals, bool accumulate)
{
  // FIXME add support for mixed-precison dot product to avoid this copy
  //if (src.Precision() != evecs[0]->Precision() && !tmp1) {
  //  quda::ColorSpinorParam param(*evecs[0]);
  //  tmp1 = new quda::ColorSpinorField(param);
  //}
  //if (sol.Precision() != evecs[0]->Precision() && !tmp2) {
  //  quda::ColorSpinorParam param(*evecs[0]);
  //  tmp2 = new quda::ColorSpinorField(param);
  //}
  quda::ColorSpinorField *tmp1, *tmp2;
  if( src.Precision() != evecs[0].Precision()){
    quda::ColorSpinorParam param(evecs[0]);
    if(evecs[0].Precision() == QUDA_DOUBLE_PRECISION){
      if(gtmp1D == NULL){gtmp1D = new quda::ColorSpinorField(param);}
      tmp1 = gtmp1D;
    }
    if(evecs[0].Precision() == QUDA_SINGLE_PRECISION){
      if(gtmp1F == NULL){gtmp1F = new quda::ColorSpinorField(param);}
      tmp1 = gtmp1F;
    }
  }
  if( sol.Precision() != evecs[0].Precision()){
    quda::ColorSpinorParam param(evecs[0]);
    if(evecs[0].Precision() == QUDA_DOUBLE_PRECISION){
      if(gtmp2D == NULL){gtmp2D = new quda::ColorSpinorField(param);}
      tmp2 = gtmp2D;
    }
    if(evecs[0].Precision() == QUDA_SINGLE_PRECISION){
      if(gtmp2F == NULL){gtmp2F = new quda::ColorSpinorField(param);}
      tmp2 = gtmp2F;
    }
  }
  quda::ColorSpinorField *src_tmp = src.Precision() != evecs[0].Precision() ? tmp1 : const_cast<quda::ColorSpinorField *>(&src);
  quda::ColorSpinorField *sol_tmp = sol.Precision() != evecs[0].Precision() ? tmp2 : const_cast<quda::ColorSpinorField *>(&sol);
  quda::blas::copy(*src_tmp, src); // no-op if these alias
  std::vector<quda::ColorSpinorField *> src_ {src_tmp};
  std::vector<quda::ColorSpinorField *> sol_ {sol_tmp};
  deflate(sol_, src_, evecs, evals, accumulate);
  quda::blas::copy(sol, *sol_tmp); // no-op if these alias
}

inline void quda_inverter::deflate(std::vector<quda::ColorSpinorField *> &sol, const std::vector<quda::ColorSpinorField *> &src,
                            std::vector<quda::ColorSpinorField> &evecs, const std::vector<quda::Complex> &evals, bool accumulate)
{
  TIMER("quda deflate");
  int n_defl = evecs.size();
  if( n_defl == 0){ return; }

  if (getVerbosity() >= QUDA_VERBOSE){printfQuda("Deflating %d vectors\n", n_defl);}

  // Perform Sum_i V_i * (L_i)^{-1} * (V_i)^dag * vec = vec_defl
  // for all i computed eigenvectors and values.

  // Pointers to the required Krylov space vectors,
  // no extra memory is allocated.
  std::vector<quda::ColorSpinorField *> eig_vecs;
  eig_vecs.reserve(n_defl);
  for (int i = 0; i < n_defl; i++) eig_vecs.push_back(&evecs[i]);

  // 1. Take block inner product: (V_i)^dag * vec = A_i
  std::vector<quda::Complex> s(n_defl * src.size());
  std::vector<quda::ColorSpinorField *> src_ = const_cast<decltype(src) &>(src);
  quda::blas::cDotProduct(s.data(), eig_vecs, src_);

  // 2. Perform block caxpy: V_i * (L_i)^{-1} * A_i
  for (int i = 0; i < n_defl; i++) { s[i] /= evals[i].real(); }

  // 3. Accumulate sum vec_defl = Sum_i V_i * (L_i)^{-1} * A_i
  if (!accumulate)
    for (auto &x : sol) quda::blas::zero(*x);
  quda::blas::caxpy(s.data(), eig_vecs, sol);

  // Save Deflation tuning
  quda::saveTuneCache();
}


inline void quda_inverter::setup_CG()
{
  solverParam.maxiter = inv_param.maxiter;
  solverParam.tol = inv_param.tol;

  if(CG_reset == false){return;}
  {
  TIMERA("setup_CG");
  clear_CG();
  QudaInvertParam& param = inv_param;
  // It was probably a bad design decision to encode whether the system is even/odd preconditioned (PC) in
  // solve_type and solution_type, rather than in separate members of QudaInvertParam.  We're stuck with it
  // for now, though, so here we factorize everything for convenience.
  bool pc_solution = (param.solution_type == QUDA_MATPC_SOLUTION) ||
    (param.solution_type == QUDA_MATPCDAG_MATPC_SOLUTION);
  bool pc_solve = (param.solve_type == QUDA_DIRECT_PC_SOLVE) ||
    (param.solve_type == QUDA_NORMOP_PC_SOLVE) || (param.solve_type == QUDA_NORMERR_PC_SOLVE);
  bool direct_solve = (param.solve_type == QUDA_DIRECT_SOLVE) ||
    (param.solve_type == QUDA_DIRECT_PC_SOLVE);

  solverParam = quda::SolverParam(param);
  solve_cg = quda::Solver::create(solverParam, *m_cg, *mSloppy, *mPre, *mEig, profileInvertC);
  }
  //if (getVerbosity() >= QUDA_VERBOSE) { printfQuda("Solution = %g\n", blas::norm2(x)); }
  CG_reset = false;
}

inline void quda_inverter::invertQuda_COPY(quda::ColorSpinorField& res, quda::ColorSpinorField& src, int solve_mode_)
{
  solverParam.secs = 0;
  solverParam.gflops = 0;
  solverParam.iter = 0;
  //inv_param.secs = 0;
  //inv_param.gflops = 0;
  //inv_param.iter = 0;

  solve_mode = solve_mode_;
  QudaInvertParam& param = inv_param;

  // It was probably a bad design decision to encode whether the system is even/odd preconditioned (PC) in
  // solve_type and solution_type, rather than in separate members of QudaInvertParam.  We're stuck with it
  // for now, though, so here we factorize everything for convenience.
  bool pc_solution = (param.solution_type == QUDA_MATPC_SOLUTION) ||
    (param.solution_type == QUDA_MATPCDAG_MATPC_SOLUTION);
  bool pc_solve = (param.solve_type == QUDA_DIRECT_PC_SOLVE) ||
    (param.solve_type == QUDA_NORMOP_PC_SOLVE) || (param.solve_type == QUDA_NORMERR_PC_SOLVE);
  bool direct_solve = (param.solve_type == QUDA_DIRECT_SOLVE) ||
    (param.solve_type == QUDA_DIRECT_PC_SOLVE);

  //quda::Dirac &dirac = *dirac_cg;
  //quda::Dirac &diracSloppy = *dSloppy;
  //quda::Dirac &diracPre = *dPre;
  //quda::Dirac &diracEig = *dEig;

  //quda::ColorSpinorField *in = nullptr;
  //quda::ColorSpinorField *out = nullptr;

  ////src b, result x
  //const bool no_clear_guess = (param.use_init_guess == QUDA_USE_INIT_GUESS_YES && !param.chrono_use_resident);
  /////->Even(), gres->Odd()
  std::vector<double > nbL;nbL.resize(num_src_inv);
  for(int di=0;di<num_src_inv;di++)
  {
    quda::ColorSpinorField& x = res.Component(di);
    quda::ColorSpinorField& b = src.Component(di);
    if(use_eigen_pc == 0){quda::blas::zero(x);}
    double& nb = nbL[di];
    nb = quda::blas::norm2(b);
    if(nb == 0.0){errorQuda("Source has zero norm");}

    if (getVerbosity() >= QUDA_VERBOSE) {
      printfQuda("Source: %g\n", nb);
      if (param.use_init_guess == QUDA_USE_INIT_GUESS_YES) { printfQuda("Initial guess: %g\n", quda::blas::norm2(x)); }
    }

    // rescale the source and solution vectors to help prevent the onset of underflow
    if (param.solver_normalization == QUDA_SOURCE_NORMALIZATION) {
      quda::blas::ax(1.0 / sqrt(nb), b);
      quda::blas::ax(1.0 / sqrt(nb), x);
    }
    quda::massRescale(b, param, false);

    if (getVerbosity() >= QUDA_VERBOSE) {
      double nin  = quda::blas::norm2(b);
      double nout = quda::blas::norm2(x);
      printfQuda("Prepared source = %g\n", nin);
      printfQuda("Prepared solution = %g\n", nout);
    }

    if (getVerbosity() >= QUDA_VERBOSE) {
      double nin = quda::blas::norm2(b);
      printfQuda("Prepared source post mass rescale = %g\n", nin);
    }
  }

  //    //*gsrc = *csrc;
  //    for(int di=0;di<num_src_inv;di++)
  //    {
  //      dirac_pc->prepare(src, sol, (*gres).Component(di), (*gsrc).Component(di), QUDA_MAT_SOLUTION);
  //    }
  //dirac.prepare(in, out, x, b, param.solution_type);

  // solution_type specifies *what* system is to be solved.
  // solve_type specifies *how* the system is to be solved.
  //
  // We have the following four cases (plus preconditioned variants):
  //
  // solution_type    solve_type    Effect
  // -------------    ----------    ------
  // MAT              DIRECT        Solve Ax=b
  // MATDAG_MAT       DIRECT        Solve A^dag y = b, followed by Ax=y
  // MAT              NORMOP        Solve (A^dag A) x = (A^dag b)
  // MATDAG_MAT       NORMOP        Solve (A^dag A) x = b
  // MAT              NORMERR       Solve (A A^dag) y = b, then x = A^dag y
  //
  // We generally require that the solution_type and solve_type
  // preconditioning match.  As an exception, the unpreconditioned MAT
  // solution_type may be used with any solve_type, including
  // DIRECT_PC and NORMOP_PC.  In these cases, preparation of the
  // preconditioned source and reconstruction of the full solution are
  // taken care of by Dirac::prepare() and Dirac::reconstruct(),
  // respectively.

  if (pc_solution && !pc_solve) {
    errorQuda("Preconditioned (PC) solution_type requires a PC solve_type");
  }

  //param->use_sloppy_partial_accumulator = 1;
  qassert(src.IsComposite());
  qassert(res.IsComposite());
  const int dim = src.CompositeDim();
  qassert(num_src_inv <= dim);
  if (direct_solve) {
    if(solve_mode == 0){
      solverParam.num_src = 1;
      for(int di=0;di<num_src_inv;di++)
      {
        (*solve_cg)(res.Component(di), src.Component(di));
      }
    }
    //if(solve_mode == 1){
    //  solverParam.num_src = num_src_inv;
    //  (*solve_cg).blocksolve(res, src);
    //}
    //if(solve_mode == 2){
    //  solverParam.num_src = num_src_inv;
    //  (*solve_cg).solve(res, src);
    //}

  }else{errorQuda("Solver not added");}


  for(int di=0;di<num_src_inv;di++)
  {
    quda::ColorSpinorField& x = res.Component(di);
    quda::ColorSpinorField& b = src.Component(di);
    double& nb = nbL[di];

    if (getVerbosity() >= QUDA_VERBOSE) { printfQuda("Solution = %g\n", quda::blas::norm2(x)); }
    ////dirac.reconstruct(x, b, param.solution_type);

    if (param.solver_normalization == QUDA_SOURCE_NORMALIZATION) {
      // rescale the solution
      quda::blas::ax(sqrt(nb), x);
    }

    if (getVerbosity() >= QUDA_VERBOSE) {
      printfQuda("Reconstructed solution: %g\n", quda::blas::norm2(x));
    }
  }
  inv_param.secs = solverParam.secs;
  inv_param.gflops = solverParam.gflops;
  quda::comm_allreduce_sum(inv_param.gflops);
  inv_param.iter = solverParam.iter;
  // cache is written out even if a long benchmarking job gets interrupted
  quda::saveTuneCache();
}


template<typename Ty>
inline void quda_inverter::do_inv(Ty* res, Ty* src, const double mass, const double err, const int niter , const int prec_type )
{
  TIMERB("QUDA CG");
  timeval tm0,tm1;gettimeofday(&tm0, NULL);gettimeofday(&tm1, NULL);

  setup_inv_param_prec(prec_type); ////restore precisions
  inv_param.tol = err;
  ///if(err < 1e-6 and err > 1e-10){inv_param.tol_restart    = err*5e+3;}
  inv_param.maxiter = niter;
  //solverParam = quda::SolverParam(inv_param);
  //maxiter, tol, 
  if(fermion_type == 0){abort_r("Not suppported!\n");setup_inv_mass(mass);}
  if(fermion_type == 1){
    setup_mat_mass(mass);
  }
  setup_CG();

  //if((void*)csrc->V() != src)qudaMemcpy((void*)csrc->V(), src, csrc->Volume() * spinor_site_size * sizeof(quda::Complex), qudaMemcpyHostToHost);
  qassert((void*) (*gsrc).V() != (void*) src);
  qlat_cf_to_quda_cf((*gsrc), src, geo, map_index);
  quda::blas::zero(*gres);

  update_eigen_mass(mass, true);
  if(use_eigen_pc == 1){

    //*gsrc = *csrc;
    //if(fermion_type == 0){
    //  if(kSpace.size()!=0){eig_solveK->deflate(*gtmp1 , *gsrc, kSpace, evalsK, false );}
    //  if(fSpace.size()!=0){eig_solveF->deflate(*gtmp1 , *gsrc, fSpace, evalsF, true  );}
    //  (*mat_Mdag)(*gres, *gtmp1);
    //  quda::blas::ax(1.0*(2.0*inv_param.kappa), *gres);
    //}

    if(fermion_type == 1){
      if(add_high == 0){
        //(*gsrc) = (*csrc);
        prepare_low_prop();
        quda_cf_to_qlat_cf(res, (*gres), geo, map_index);
        //(*cres) = (*gres);
        //if((void*)cres->V() != res){qudaMemcpy(res, (void*)cres->V(), 
        //        cres->Volume() * spinor_site_size * sizeof(quda::Complex), qudaMemcpyHostToHost);}
        gettimeofday(&tm1, NULL);double time0 = tm1.tv_sec - tm0.tv_sec;time0 += (tm1.tv_usec - tm0.tv_usec)/1000000.0;
        if(quda::comm_rank_global() == 0)printfQuda("prepare low Done:  %.6f secs \n", time0);
        return ;
      }

      quda::ColorSpinorField *srcP;
      quda::ColorSpinorField *sol0;
      quda::ColorSpinorField *sol1;

      for(int di=0;di<num_src_inv;di++)
      {
        dirac_pc->prepare(srcP, sol0, (*gtmp0).Component(di), (*gsrc).Component(di), QUDA_MAT_SOLUTION);
        dirac_pc->prepare(srcP, sol1, (*gres ).Component(di), (*gsrc).Component(di), QUDA_MAT_SOLUTION);
        quda::blas::zero(*sol0);quda::blas::zero(*sol1);
        if(kSpace.size()!=0){deflate((*sol0), (*srcP), kSpace, evalsK, false);}
        if(fSpace.size()!=0){deflate((*sol1), (*srcP), fSpace, evalsF, false);}

        quda::Complex lambda  = quda::Complex(1.0, 0.0);
        if(kSpace.size()!=0){lambda  = lambda - quda::blas::cDotProduct(*sol0, *sol1) / quda::blas::norm2(*sol0);}
        quda::blas::caxpy(lambda, *sol0, *sol1);
      }

      //dirac_pc->prepare(src, sol0, (*gres ), (*gsrc), QUDA_MAT_SOLUTION);
      //quda::blas::zero(*sol0);
      //if(kSpace.size()!=0){eig_solveK->deflate(*sol0 , *src, kSpace, evalsK, false );}
      //if(fSpace.size()!=0){eig_solveF->deflate(*sol0 , *src, fSpace, evalsF, true  );}

      /////preconditioning to single and back to double to match AMA prec
      //if(add_high == 0){*gsrcF = *gres;*gres = *gsrcF;}

    }
    //*cres = *gres;

  }else{
    if(fermion_type == 1){
      quda::ColorSpinorField *srcP;
      quda::ColorSpinorField *solP;

      //const size_t Nd = (*gsrc).Component(0).Volume() * spinor_site_size * sizeof(quda::Complex);
      //qlat::vector_acc<qlat::Complex > buf;buf.resize(Nd/sizeof(quda::Complex));
      ////*gsrc = *csrc;
      for(int di=0;di<num_src_inv;di++)
      {
        //qudaMemcpy((void*) buf.data(), &src[di*Nd/sizeof(quda::Complex)], Nd, qudaMemcpyDeviceToHost);
        //qlat_cf_to_quda_cf((qlat::Complex*) ctmp0->Component(di).V(), (qlat::Complex*) buf.data(), geo, 3);
        //(*gsrc).Component(di) = (*ctmp0).Component(di);
        dirac_pc->prepare(srcP, solP, (*gres).Component(di), (*gsrc).Component(di), QUDA_MAT_SOLUTION);
        //(*ctmp1).Component(di) = (*gres).Component(di);
      }
      //qlat_cf_to_quda_cf((qlat::Complex*) ctmp1->V(), src, geo, Dim);
      //*cres = *gres;
    }
  }

  //if(fermion_type == 0){invertQuda((void*)(cres->Even()).V(), (void*)(csrc->Even()).V(), &inv_param);}
  if(fermion_type == 1){
    inv_param.solution_type = QUDA_MATPC_SOLUTION;

    if(add_high >= 1){
      //invertQuda((void*)((*ctmp1).Component(0).Even()).V(), (void*)((*ctmp1).Component(0).Odd()).V(), &inv_param);
      for(int di=0;di<num_src_inv;di++)
      {
        (*gresH).Component(di) = (*gres).Component(di).Even();
        (*gsrcH).Component(di) = (*gres).Component(di).Odd();
      }

      invertQuda_COPY(*gresH, *gsrcH, solve_mode);

      for(int di=0;di<num_src_inv;di++)
      {
        (*gres).Component(di).Even() = (*gresH).Component(di);
        (*gres).Component(di).Odd()  = (*gsrcH).Component(di);
      }

      //quda::ColorSpinorParam cs_cpu1 = quda::ColorSpinorParam(*gsrcH);
      //cs_cpu1.location = QUDA_CPU_FIELD_LOCATION;
      //cs_cpu1.is_composite  = false;
      //cs_cpu1.is_component  = false;

      //quda::ColorSpinorField csrc(cs_cpu1);
      //quda::ColorSpinorField cres(cs_cpu1);

      //const size_t Nd = (*gsrcH).Component(0).Volume() * spinor_site_size * sizeof(quda::Complex);
      //qudaMemcpy((void*)cres.V(), (*gresH).Component(0).V(), Nd, qudaMemcpyDeviceToHost);
      //qudaMemcpy((void*)csrc.V(), (*gsrcH).Component(0).V(), Nd, qudaMemcpyDeviceToHost);
      ////csrc = (*gsrcH).Component(0);
      ////cres = (*gresH).Component(0); 
      //invertQuda((void*)(cres).V(), (void*)(csrc).V(), &inv_param);
      //qudaMemcpy((*gresH).Component(0).V(), (void*)cres.V(), Nd, qudaMemcpyHostToDevice);
      //qudaMemcpy((*gsrcH).Component(0).V(), (void*)csrc.V(), Nd, qudaMemcpyHostToDevice);

      ////(*gsrcH).Component(0) = csrc;
      ////(*gresH).Component(0) = cres; 

    }

    //*gres = *cres;
    //*gres = *ctmp1;
    for(int di=0;di<num_src_inv;di++)
    {
      //(*gres).Component(di) = (*ctmp1).Component(di);
      dirac_pc->reconstruct((*gres).Component(di), (*gsrc).Component(di), QUDA_MAT_SOLUTION);
    }

    //*cres = *gres;
    inv_param.solution_type = QUDA_MAT_SOLUTION;
  }

  if(check_residue == 1)
  { 
    /////TODO not working for multi GPU
    /////===check residue
    quda::Complex n_unit(-1.0, 0.0);
    
    quda::ColorSpinorParam cs_gpu1 = quda::ColorSpinorParam(*gres);
    cs_gpu1.is_composite  = false;
    cs_gpu1.is_component  = false;

    quda::ColorSpinorField buf(cs_gpu1);
    for(int di=0;di<num_src_inv;di++){
      quda::ColorSpinorField& src = (*gsrc).Component(di);
      quda::ColorSpinorField& res = (*gres).Component(di);
      quda::blas::zero(buf);
      (*mat)((buf), res);

      qacc_barrier(dummy);
      quda::Complex temp = quda::blas::norm2(res);
      ////if(quda::comm_rank_global()== 0)printf("===result %.8e \n", temp.real());

      if(fermion_type == 0){quda::blas::ax(1.0/(2.0*inv_param.kappa), buf);}

      quda::Complex evals  = quda::blas::cDotProduct(src, buf) / quda::blas::norm2(src);
      quda::Complex factor = sqrt(quda::blas::norm2(buf)) / sqrt(quda::blas::norm2(src));
      quda::blas::caxpby(evals, src , n_unit, buf);
      //if(fermion_type == 1){
      //}
      quda::Complex residual = sqrt(quda::blas::norm2(buf)/ quda::blas::norm2(src));
      quda::Complex nor_e1 = sqrt( quda::blas::norm2((res).Even()));
      quda::Complex nor_o1 = sqrt( quda::blas::norm2((res).Odd() ));

      quda::Complex nor_e = sqrt( quda::blas::norm2((src).Even()));
      quda::Complex nor_o = sqrt( quda::blas::norm2((src).Odd() ));
      quda::Complex res_e = sqrt(quda::blas::norm2((buf).Even())/ quda::blas::norm2((src)));
      quda::Complex res_o = sqrt(quda::blas::norm2((buf).Odd())/ quda::blas::norm2((src)));

      if(quda::comm_rank_global()== 0)printf("===solution residual %.3e, factor %.3e, sol norm %.8e, e %.8e , o %.8e \n", 
            residual.real(), factor.real(), temp.real(), res_e.real(), res_o.real());

      //if(quda::comm_rank_global()== 0)printf("===solution residual %.3e, factor %.3e, sol norm %.8e, e %.8e %.3e %.3e, o %.8e %.3e %.3e \n", 
      //      residual.real(), factor.real(), temp.real(), res_e.real(), nor_e1.real(), nor_e.real(), res_o.real(), nor_o1.real(), nor_o.real());
      inv_residue = residual.real();
    }

    //qacc_barrier(dummy);
    //fflush_MPI();
    ////std::vector<quda::Complex> sump(3);
    ////quda::comm_allreduce_sum(sump);
    /////===check residue
  }
  //if((void*)cres->V() != res){qudaMemcpy(res, (void*)cres->V(), cres->Volume() * spinor_site_size * sizeof(quda::Complex), qudaMemcpyHostToHost);}
  qassert((void*) (*gres).V() != (void*) res);
  //*ctmp0 = *gres;
      //const size_t Nd = (*gsrc).Component(0).Volume() * spinor_site_size * sizeof(quda::Complex);
      //qlat::vector_acc<qlat::Complex > buf;buf.resize(Nd/sizeof(quda::Complex));
      //for(int di=0;di<num_src_inv;di++){
      //  quda_cf_to_qlat_cf((qlat::Complex*) buf.data(), (qlat::Complex*) ctmp0->Component(di).V(), geo, 3);
      //  qudaMemcpy(&res[di*Nd/sizeof(quda::Complex)], (void*) buf.data(), Nd, qudaMemcpyDeviceToDevice);
      //}
  quda_cf_to_qlat_cf(res, (*gres), geo, map_index);

  ////{errorQuda("QUDA may have bugs right now for the code on CUDA FIELD below\n");}

  gettimeofday(&tm1, NULL);double time0 = tm1.tv_sec - tm0.tv_sec;time0 += (tm1.tv_usec - tm0.tv_usec)/1000000.0;

  int verbos = 0;
  inv_param.secs += 1e-25;
  std::string val = qlat::get_env(std::string("qlat_quda_verbos"));
  if(val != ""){verbos = stringtonum(val);}
  if(verbos != -1)
  if(quda::comm_rank_global() == 0)printfQuda("Done: %8d iter / %.6f secs = %.3f Gflops, Cost %.3f Gflops, %.6f secs \n",
          inv_param.iter, inv_param.secs, inv_param.gflops / inv_param.secs, inv_param.gflops, time0);
  inv_time   = time0;
  inv_iter   = inv_param.iter;
  inv_gflops = inv_param.gflops / inv_param.secs;

  /////setup_inv_param_prec(); ////restore precisions

  ////quda::saveTuneCache();
}

quda_inverter::~quda_inverter()
{
  free_mem();
}

template<typename Ty>
void get_staggered_prop(quda_inverter& qinv, Ty* src, Ty* prop, 
    const double mass, const double err, const int niter, int low_only = 0, const int prec_type = 0)
{
  TIMER("QUDA inversions");
  if(qinv.fermion_type == 0)qinv.setup_inv_mass(mass);
  if(qinv.fermion_type == 1)qinv.setup_mat_mass(mass);
  //const int Dim = 3;
  //qlat_cf_to_quda_cf((qlat::Complex*) qinv.csrc->V(), src, geo, Dim);

  //{
  //const long V = qinv.geo.local_volume();
  //qlat::vector_gpu<Ty > tmp;tmp.resize(V*3);
  //tmp.copy_from(src, V*3);
  //Ty norm = tmp.norm();
  //print0("==src norm %.8e \n", norm.real());
  //}

  //Ty norm = norm_FieldM(prop);
  //print0("normp %.3e %.3e \n", norm.real(), norm.imag());
  if(low_only == 0){
    //qinv.do_inv(qinv.cres->V(), qinv.csrc->V(), mass, err, niter, prec_type);
    qinv.do_inv(prop, src, mass, err, niter, prec_type);
  }

  if(low_only == 1){
    qlat_cf_to_quda_cf((*qinv.gsrc), src, qinv.geo, qinv.map_index);
    qinv.prepare_low_prop();
    quda_cf_to_qlat_cf(prop, (*qinv.gres), qinv.geo, qinv.map_index);
  }

  if(low_only == 2){
    if(qinv.gadd == NULL){
      quda::ColorSpinorParam param(*qinv.gres);
      qinv.gadd  = quda::ColorSpinorField::Create(param);
    }
    qlat_cf_to_quda_cf((*qinv.gtmp0), src, qinv.geo, qinv.map_index);

    qinv.do_inv(prop, src, mass, err, niter, prec_type);
    //qinv.do_inv(qinv.cres->V(), qinv.csrc->V(), mass, err, niter, prec_type);
    (*qinv.gadd) = (*qinv.gres);

    (*qinv.gsrc) = (*qinv.gtmp0);
    qinv.prepare_low_prop();

    quda::Complex n_unit(+1.0, 0.0);
    quda::Complex p_unit(-1.0, 0.0);
    quda::blas::caxpby(n_unit, *qinv.gadd  , p_unit, *qinv.gres);
    //(*qinv.cres) = (*qinv.gres);
    quda_cf_to_qlat_cf(prop, (*qinv.gres), qinv.geo, qinv.map_index);
  }
}


template<typename Ty>
void get_staggered_prop(quda_inverter& qinv, qlat::FieldM<Ty, 3>& src, qlat::FieldM<Ty, 3>& prop
    , const double mass, const double err, const int niter, int low_only = 0, const int prec_type = 0)
{
  Ty* srcP = (Ty*) qlat::get_data(src).data();

  const Geometry& geo = src.geo();
  if(!prop.initialized){prop.init(geo);} ////allocate mem for prop
  Ty* propP = (Ty*) qlat::get_data(prop).data();

  get_staggered_prop(qinv, srcP, propP, mass, err, niter, low_only, prec_type);
  //   norm = norm_FieldM(prop);
  //print0("normp %.3e %.3e \n", norm.real(), norm.imag());
}

template<typename Ty>
void get_staggered_prop(quda_inverter& qinv, std::vector<qlat::FieldM<Ty, 3> >& srcL, std::vector<qlat::FieldM<Ty, 3> >& propL
    , const double mass, const double err, const int niter, int low_only = 0, const int prec_type = 0)
{
  const int Ninv = srcL.size();
  if(Ninv <= 0){propL.resize(0);return ;}
  for(int iv=0;iv<Ninv;iv++)
  {
    get_staggered_prop(qinv,srcL[iv], propL[iv], mass, err, niter, low_only, prec_type);
  }
}

template<typename Ty>
void get_staggered_prop(quda_inverter& qinv, qlat::vector_gpu<Ty >& src, qlat::vector_gpu<Ty >& prop,
    const double mass, const double err, const int niter, int low_only = 0, const int prec_type = 0)
{
  const size_t Vl = qinv.V * 3;
  qassert(src.size() % Vl == 0);
  prop.resize(src.size());
  const int Ninv = src.size() / Vl;
  if(Ninv <= 0){prop.resize(0);return ;}

  qassert(Ninv <= qinv.num_src);
  int tmp_inv = qinv.num_src_inv;
  qinv.num_src_inv = Ninv;

  Ty* srcP = src.data();
  Ty* resP = prop.data();
  move_index mv_civ;
  mv_civ.move_civ_out(srcP, resP, 1, Vl, 3, 1, true);
  get_staggered_prop(qinv, resP, resP,  mass, err, niter, low_only, prec_type);
  mv_civ.move_civ_in( resP, resP, 1, 3, Vl, 1, true);

  //std::vector<colorFT > srcP;srcP.resize(3);
  //for(int i=0;i<3;i++){srcP[i].init(qinv.geo);}
  //qassert(Ninv == 3);
  //for(int iv=0;iv<Ninv;iv++)
  //{
  //  copy_to_color_prop(srcP, src);
  //  get_staggered_prop(qinv, srcP, srcP,  mass, err, niter, low_only, prec_type);
  //  copy_color_prop(prop, srcP);
  //}
  qinv.num_src_inv = tmp_inv;
}



}  // namespace qlat



#endif


