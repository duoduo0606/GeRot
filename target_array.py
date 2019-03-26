from Target_Generator import TargetGene
import numpy as np

width = 30
height = 50
depth = 10
gecko = TargetGene()
gecko.present_position = {'rf': np.array([gecko.L1, gecko.L2 - width/2, -gecko.L3]),
                          'rh': np.array([gecko.L1, gecko.L2, -gecko.L3 - 10]),
                          'lf': np.array([gecko.L1, gecko.L2 - width/2, -gecko.L3]),
                          'lh': np.array([gecko.L1, gecko.L2, -gecko.L3 - 10])}

# step 0
p_detach, v_detach = gecko.detach('rf', 2, 0.01, width, height)
p_moving0, v_moving0 = gecko.moving('rf', 1, 0.01, np.array([gecko.L1, gecko.present_position['rf'][1],
                                                             gecko.present_position['rf'][2] - (height + depth)]))
p_moving1, v_moving1 = gecko.moving('rf', 0.2, 0.01, np.array([gecko.L1, gecko.present_position['rf'][1],
                                                               gecko.present_position['rf'][2] + depth]))
rf_target_p = np.vstack((p_detach, p_moving0, p_moving1))
rf_target_v = np.vstack((v_detach, v_moving0, v_moving1))


rh_target_p, rh_target_v = gecko.steady('rh', int(rf_target_p.shape[0]))
lf_target_p, lf_target_v = gecko.steady('lf', int(rf_target_p.shape[0]))
lh_target_p, lh_target_v = gecko.steady('lh', int(rf_target_p.shape[0]))

target_p0 = np.hstack((rf_target_p, rh_target_p, lf_target_p, lh_target_p))
target_v0 = np.hstack((rf_target_v, rh_target_v, lf_target_v, lh_target_v))

# step 1
p_detach, v_detach = gecko.detach('lf', 2, 0.01, width, height)
p_moving0, v_moving0 = gecko.moving('lf', 1, 0.01, np.array([gecko.L1, gecko.present_position['lf'][1],
                                                             gecko.present_position['lf'][2] - (height + depth)]))
p_moving1, v_moving1 = gecko.moving('lf', 0.2, 0.01, np.array([gecko.L1, gecko.present_position['lf'][1],
                                                               gecko.present_position['lf'][2] + depth]))
lf_target_p = np.vstack((p_detach, p_moving0, p_moving1))
lf_target_v = np.vstack((v_detach, v_moving0, v_moving1))


rh_target_p, rh_target_v = gecko.steady('rh', int(lf_target_p.shape[0]))
rf_target_p, rf_target_v = gecko.steady('rf', int(lf_target_p.shape[0]))
lh_target_p, lh_target_v = gecko.steady('lh', int(lf_target_p.shape[0]))

target_p1 = np.hstack((rf_target_p, rh_target_p, lf_target_p, lh_target_p))
target_v1 = np.hstack((rf_target_v, rh_target_v, lf_target_v, lh_target_v))

# moving 0
rf_target_p, rf_target_v = gecko.moving('rf', 1, 0.01, np.array([gecko.L1, gecko.present_position['rf'][1] - width/2,
                                                                 gecko.present_position['rf'][2]]))
rh_target_p, rh_target_v = gecko.moving('rh', 1, 0.01, np.array([gecko.L1, gecko.present_position['rh'][1] - width/2,
                                                                 gecko.present_position['rh'][2]]))
lf_target_p, lf_target_v = gecko.moving('lf', 1, 0.01, np.array([gecko.L1, gecko.present_position['lf'][1] - width/2,
                                                                 gecko.present_position['lf'][2]]))
lh_target_p, lh_target_v = gecko.moving('lh', 1, 0.01, np.array([gecko.L1, gecko.present_position['lh'][1] - width/2,
                                                                 gecko.present_position['lh'][2]]))
target_p_m0 = np.hstack((rf_target_p, rh_target_p, lf_target_p, lh_target_p))
target_v_m0 = np.hstack((rf_target_v, rh_target_v, lf_target_v, lh_target_v))

# step 2
p_detach, v_detach = gecko.detach('rh', 2, 0.01, width, height)
p_moving0, v_moving0 = gecko.moving('rh', 1, 0.01, np.array([gecko.L1, gecko.present_position['rh'][1],
                                                             gecko.present_position['rh'][2] - (height + depth)]))
p_moving1, v_moving1 = gecko.moving('rh', 0.2, 0.01, np.array([gecko.L1, gecko.present_position['rh'][1],
                                                               gecko.present_position['rh'][2] + depth]))
rh_target_p = np.vstack((p_detach, p_moving0, p_moving1))
rh_target_v = np.vstack((v_detach, v_moving0, v_moving1))

rf_target_p, rf_target_v = gecko.steady('rf', int(rh_target_p.shape[0]))
lf_target_p, lf_target_v = gecko.steady('lf', int(rh_target_p.shape[0]))
lh_target_p, lh_target_v = gecko.steady('lh', int(rh_target_p.shape[0]))

target_p2 = np.hstack((rf_target_p, rh_target_p, lf_target_p, lh_target_p))
target_v2 = np.hstack((rf_target_v, rh_target_v, lf_target_v, lh_target_v))

# step 3
p_detach, v_detach = gecko.detach('lh', 2, 0.01, width, height)
p_moving0, v_moving0 = gecko.moving('lh', 1, 0.01, np.array([gecko.L1, gecko.present_position['lh'][1],
                                                             gecko.present_position['lh'][2] - (height + depth)]))
p_moving1, v_moving1 = gecko.moving('lh', 0.2, 0.01, np.array([gecko.L1, gecko.present_position['lh'][1],
                                                               gecko.present_position['lh'][2] + depth]))
lh_target_p = np.vstack((p_detach, p_moving0, p_moving1))
lh_target_v = np.vstack((v_detach, v_moving0, v_moving1))


rf_target_p, rf_target_v = gecko.steady('rf', int(rh_target_p.shape[0]))
lf_target_p, lf_target_v = gecko.steady('lf', int(rh_target_p.shape[0]))
rh_target_p, rh_target_v = gecko.steady('rh', int(rh_target_p.shape[0]))

target_p3 = np.hstack((rf_target_p, rh_target_p, lf_target_p, lh_target_p))
target_v3 = np.hstack((rf_target_v, rh_target_v, lf_target_v, lh_target_v))

# moving 1
rf_target_p, rf_target_v = gecko.moving('rf', 1, 0.01, np.array([gecko.L1, gecko.present_position['rf'][1] - width/2,
                                                                 gecko.present_position['rf'][2]]))
rh_target_p, rh_target_v = gecko.moving('rh', 1, 0.01, np.array([gecko.L1, gecko.present_position['rh'][1] - width/2,
                                                                 gecko.present_position['rh'][2]]))
lf_target_p, lf_target_v = gecko.moving('lf', 1, 0.01, np.array([gecko.L1, gecko.present_position['lf'][1] - width/2,
                                                                 gecko.present_position['lf'][2]]))
lh_target_p, lh_target_v = gecko.moving('lh', 1, 0.01, np.array([gecko.L1, gecko.present_position['lh'][1] - width/2,
                                                                 gecko.present_position['lh'][2]]))
target_p_m1 = np.hstack((rf_target_p, rh_target_p, lf_target_p, lh_target_p))
target_v_m1 = np.hstack((rf_target_v, rh_target_v, lf_target_v, lh_target_v))

target_p = np.vstack((target_p0, target_p1, target_p_m0, target_p2, target_p3, target_p_m1))
target_v = np.vstack((target_v0, target_v1, target_v_m0, target_v2, target_v3, target_v_m1))

np.savetxt('target_p.csv', target_p, delimiter=',')
np.savetxt('target_v.csv', target_v, delimiter=',')




