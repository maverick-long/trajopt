  #ifndef KINEMATICS_TERMS_HPP
#define KINEMATICS_TERMS_HPP

#pragma once

#include "sco/modeling.hpp"
#include "sco/modeling_utils.hpp"
#include "sco/sco_fwd.hpp"
#include <Eigen/Core>
#include "trajopt/common.hpp"
#include <openrave/openrave.h>
namespace trajopt {

using namespace sco;
typedef BasicArray<Var> VarArray;

#if 0
void makeTrajVariablesAndBounds(int n_steps, const RobotAndDOF& manip, OptProb& prob_out, VarArray& vars_out);

class FKFunc {
public:
  virtual OpenRAVE::Transform operator()(const VectorXd& x) const = 0;
  virtual ~FKFunc() {}
};

class FKPositionJacobian {
public:
  virtual Eigen::MatrixXd operator()(const VectorXd& x) const = 0;
  virtual ~FKPositionJacobian() {}
};
#endif


struct CartPoseErrCalculator : public VectorOfVector {
  OR::Transform pose_inv_;
  ConfigurationPtr manip_;
  OR::KinBody::LinkPtr link_;
  Vector3d offset_;
  CartPoseErrCalculator(const OR::Transform& pose, ConfigurationPtr manip, OR::KinBody::LinkPtr link,Eigen::Vector3d offset) :
    pose_inv_(pose.inverse()),
    manip_(manip),
    link_(link),
    offset_(offset){}
  VectorXd operator()(const VectorXd& dof_vals) const;
};

struct CartPoseErrorPlotter : public Plotter {
  boost::shared_ptr<void> m_calc; //actually points to a CartPoseErrCalculator = CartPoseCost::f_
  VarVector m_vars;
  CartPoseErrorPlotter(boost::shared_ptr<void> calc, const VarVector& vars) : m_calc(calc), m_vars(vars) {}
  void Plot(const DblVec& x, OR::EnvironmentBase& env, std::vector<OR::GraphHandlePtr>& handles);
};

struct  PushSupportPolygonErrCalculator: public VectorOfVector
{
  ConfigurationPtr manip_;
  OR::KinBody::LinkPtr link_;
  Vector3d offset_;
  PushSupportPolygonErrCalculator(ConfigurationPtr manip, OR::KinBody::LinkPtr link,  Eigen::Vector3d offset) :
    manip_(manip),
    link_(link),
    offset_(offset){}
  VectorXd operator()(const VectorXd& dof_vals) const;
};

struct PushSupportPolygonOneFootErrCalculator : public VectorOfVector 
{
  ConfigurationPtr manip_;
  OR::KinBody::LinkPtr link_;
  OR::Transform fixed_foot_transform_;
  PushSupportPolygonOneFootErrCalculator(const OR::Transform& fixed_foot_transform, ConfigurationPtr manip, OR::KinBody::LinkPtr link) :
  fixed_foot_transform_(fixed_foot_transform),
  manip_(manip),
  link_(link){}
  VectorXd operator()(const VectorXd& dof_vals) const;
};

struct TwolinksCartPoseErrCalculator : public VectorOfVector
{
  OR::Transform transform_;
  ConfigurationPtr manip_;
  OR::KinBody::LinkPtr link1_;
  OR::KinBody::LinkPtr link2_;
  TwolinksCartPoseErrCalculator(const OR::Transform& transform, ConfigurationPtr manip, OR::KinBody::LinkPtr link1,  OR::KinBody::LinkPtr link2) :
    transform_(transform),
    manip_(manip),
    link1_(link1),
    link2_(link2){}
  VectorXd operator()(const VectorXd& dof_vals) const;
};

struct CartDDPoseErrCalculator : public VectorOfVector {
  ConfigurationPtr manip_;
  OR::KinBody::LinkPtr link_;
  Vector3d offset_;
  CartDDPoseErrCalculator(ConfigurationPtr manip, OR::KinBody::LinkPtr link,Eigen::Vector3d offset) :
  manip_(manip),
  link_(link),
  offset_(offset){}
  VectorXd operator()(const VectorXd& dof_vals) const;
};

struct CartPoseConstraintCalculator : public VectorOfVector {
	OR::Vector plane1_;
	OR::Vector plane2_;
	OR::Vector normal_;
	ConfigurationPtr manip_;
	OR::KinBody::LinkPtr link_;
	CartPoseConstraintCalculator(const OR::Vector plane1, const OR::Vector plane2, ConfigurationPtr manip, OR::KinBody::LinkPtr link) :
	plane1_(plane1),
	plane2_(plane2),
    manip_(manip),
	link_(link)
	{normal_ = (plane1 - plane2).normalize();}
	VectorXd operator()(const VectorXd& dof_vals) const;

};

struct CartVelJacCalculator : MatrixOfVector {
  ConfigurationPtr manip_;
  KinBody::LinkPtr link_;
  double limit_;
  CartVelJacCalculator(ConfigurationPtr manip, KinBody::LinkPtr link, double limit) :
    manip_(manip), link_(link), limit_(limit) {}

  MatrixXd operator()(const VectorXd& dof_vals) const;
};

struct CartVelCalculator : VectorOfVector {
  ConfigurationPtr manip_;
  KinBody::LinkPtr link_;
  double limit_;
  CartVelCalculator(ConfigurationPtr manip, KinBody::LinkPtr link, double limit) :
    manip_(manip), link_(link), limit_(limit) {}

  VectorXd operator()(const VectorXd& dof_vals) const;
};

#if 0
class CartPoseCost : public CostFromErrFunc {
public:
  CartPoseCost(const VarVector& vars, const OR::Transform& pose, RobotAndDOFPtr manip, KinBody::LinkPtr link, const VectorXd& coeffs);
};

class CartPoseConstraint : public ConstraintFromFunc {
public:
  CartPoseConstraint(const VarVector& vars, const OR::Transform& pose, RobotAndDOFPtr manip, KinBody::LinkPtr link, const VectorXd& coeffs);
};

class CartVelConstraint : public ConstraintFromFunc {
public:
  CartVelConstraint(const VarVector& step0vars, const VarVector& step1vars, RobotAndDOFPtr manip, KinBody::LinkPtr link, double distlimit);
};
#endif



}

#endif // KINEMATIC_TERMS_HPP
